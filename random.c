#include <stdio.h>

#define N 128         // Matrix size
#define BLOCK_SIZE 16 // Block size

__global__ void matrixMulGlobal(float *A, float *B, float *C)
{
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    if (row < N && col < N)
    {
        float sum = 0.0f;
        for (int i = 0; i < N; ++i)
        {
            sum += A[row * N + i] * B[i * N + col];
        }
        C[row * N + col] = sum;
    }
}

__global__ void matrixMulShared(float *A, float *B, float *C)
{
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;

    __shared__ float shared_A[BLOCK_SIZE][BLOCK_SIZE];
    __shared__ float shared_B[BLOCK_SIZE][BLOCK_SIZE];

    float sum = 0.0f;

    for (int m = 0; m < N / BLOCK_SIZE; ++m)
    {
        shared_A[threadIdx.y][threadIdx.x] = A[row * N + m * BLOCK_SIZE + threadIdx.x];
        shared_B[threadIdx.y][threadIdx.x] = B[(m * BLOCK_SIZE + threadIdx.y) * N + col];
        __syncthreads();

        for (int k = 0; k < BLOCK_SIZE; ++k)
        {
            sum += shared_A[threadIdx.y][k] * shared_B[k][threadIdx.x];
        }
        __syncthreads();
    }

    if (row < N && col < N)
    {
        C[row * N + col] = sum;
    }
}

int main()
{
    float *h_A, *h_B, *h_C; // Host matrices
    float *d_A, *d_B, *d_C; // Device matrices

    size_t matrix_size = N * N * sizeof(float);

    // Allocate host memory
    h_A = (float *)malloc(matrix_size);
    h_B = (float *)malloc(matrix_size);
    h_C = (float *)malloc(matrix_size);

    // Initialize matrices h_A and h_B

    // Allocate device memory
    cudaMalloc((void **)&d_A, matrix_size);
    cudaMalloc((void **)&d_B, matrix_size);
    cudaMalloc((void **)&d_C, matrix_size);

    // Copy host matrices to device
    cudaMemcpy(d_A, h_A, matrix_size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B, matrix_size, cudaMemcpyHostToDevice);

    // Launch kernel for global memory matrix multiplication
    dim3 globalGrid(N / BLOCK_SIZE, N / BLOCK_SIZE);
    dim3 globalBlock(BLOCK_SIZE, BLOCK_SIZE);
    matrixMulGlobal<<<globalGrid, globalBlock>>>(d_A, d_B, d_C);
    cudaDeviceSynchronize();

    // Copy result matrix back to host
    cudaMemcpy(h_C, d_C, matrix_size, cudaMemcpyDeviceToHost);

    // Launch kernel for shared memory matrix multiplication
    dim3 sharedGrid(N / BLOCK_SIZE, N / BLOCK_SIZE);
    dim3 sharedBlock(BLOCK_SIZE, BLOCK_SIZE);
    matrixMulShared<<<sharedGrid, sharedBlock>>>(d_A, d_B, d_C);
    cudaDeviceSynchronize();

    // Copy result matrix back to host
    cudaMemcpy(h_C, d_C, matrix_size, cudaMemcpyDeviceToHost);

    // Free memory
    free(h_A);
    free(h_B);
    free(h_C);
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    return 0;
}
