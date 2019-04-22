#include "papi.h"
#include <stdlib.h>
#include <stdio.h>
int main() {
int EventSet;
char name[64];
int i, sum;
long_long values[9], values1[9], values2[9];
if (PAPI_library_init(PAPI_VER_CURRENT) != PAPI_VER_CURRENT){
printf("init error");
exit(-1);
}
EventSet = PAPI_NULL;

if (PAPI_create_eventset(&EventSet) != PAPI_OK){
printf("create error");
exit(-1);

}

	if (PAPI_add_event(EventSet, PAPI_L1_TCM) != PAPI_OK){
printf("add1 error");
exit(-1);}
	if (PAPI_add_event(EventSet, PAPI_TLB_DM) != PAPI_OK){
printf("add2 error");
exit(-1);}
	if (PAPI_add_event(EventSet, PAPI_FUL_ICY) != PAPI_OK){
printf("add3 error");
exit(-1);}




if (PAPI_start(EventSet) != PAPI_OK){
printf("start error");
exit(-1);}
if (PAPI_read(EventSet, values1) != PAPI_OK){
printf("read error");
exit(-1);}




     printf("your name");
     scanf("%s",name);
     printf("Hello,%s%ld!\n",name,random());



if (PAPI_stop(EventSet, values2) != PAPI_OK){
printf("stop error");
exit(-1);
}
if (PAPI_cleanup_eventset(EventSet) != PAPI_OK){
printf("clean error");
exit(-1);
}
if (PAPI_destroy_eventset(&EventSet) != PAPI_OK){
printf("destroy error");
exit(-1);
}
PAPI_shutdown();

/* Get value */


values[0]=values2[0]-values1[0];
values[1]=values2[1]-values1[1];
values[2]=values2[2]-values1[2];
values[3]=values2[3]-values1[3];
values[4]=values2[4]-values1[4];
values[5]=values2[5]-values1[5];
values[6]=values2[6]-values1[6];
values[7]=values2[7]-values1[7];
values[8]=values2[8]-values1[8];









printf("L1_TCM: %lld\nTLB_DM:%lld\n",values[0], values[1]);
printf("PAPI_FUL_ICY: %lld\nPAPI_BR_UCN:%lld\n",values[2], values[3]);
printf("PAPI_BR_TKN: %lld\nPAPI_BR_PRC:%lld\n",values[4], values[5]);
printf("PAPI_LST_INS: %lld\nPAPI_L2_TCA:%lld\n",values[6], values[7]);
printf("PAPI_L2_TCR: %lld\n",values[8]);





return 0;

}
