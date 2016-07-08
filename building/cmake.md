-------------------- fun.cpp --------------------

int add(int a,int b){
    return a+b;
}



// fun.h

int add(int a,int b);



-------------------- main.cpp --------------------

#include "fun.h"
#include <stdio.h>

int main(){
    int ans=add(1,2);
    printf("ans=%d",ans);
    return 0;
}

# 參考資料
