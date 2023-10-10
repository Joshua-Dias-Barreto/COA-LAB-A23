#ifndef WARP_STATE_COUNTER
#define WARP_STATE_COUNTER

// Defining custom indexes for the counter array
enum counters { CYCLE, WAITING, ISSUED, XALU, XMEM, OTHER };

// Counter array size
#define NUM_COUNTERS (OTHER + 1)

// Declaring the counter array
extern unsigned long long warp_state_counters[NUM_COUNTERS];

#endif