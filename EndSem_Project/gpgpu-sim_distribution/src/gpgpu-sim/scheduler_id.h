#ifndef __SCHEDULER_ID_H__
#define __SCHEDULER_ID_H__

enum SchedulerID {
  OCU_MEM,
  OCU_SP,
  OCU_SFU,
  OCU_TENSOR_CORE,
  OCU_DP,
  OCU_INT,
  OCU_SPEC,
  END_OF_SCHEDULER_ID
};

#endif