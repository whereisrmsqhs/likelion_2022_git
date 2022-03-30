#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX 1250

char buffer[MAX]={0,};

float find_frequency(int key_length, int input_length){         //ex) key길이가 2이면 문자열 2개 생성
    char ASCII_distribution[95];                                //32번 스페이스부터 ~ 126번 ~까지임으로, 인덱스 0은 32번임을 설정해야함
    int max_stream_length = MAX / key_length;                   
    char** streams;
    int overlap = 0;
    float fraction = 0;
    float numerator = input_length / key_length;
    float* distribution = (float*)malloc(sizeof(float)*key_length);     //잘라진 streams들의 각 distribution값 저장

    streams = (char**)malloc(sizeof(char*)*key_length);          //문자열 2개 할당
    int k=0;
    for(int i = 0; i < key_length;i++){
        streams[i] = (char*)malloc(sizeof(char) * max_stream_length);
    }

    for(int i = 0 ; i < key_length; i++){                        
        for(int j = i; j < input_length ;j+=key_length){
            streams[i][k] = buffer[j];
            printf("%c ", streams[i][k]);
            k++;
        }
        k=0;
        printf("\n");
    }


    // 0.065근사 값이 나와야 하는데...   Igomm#bpzqvl!ulsng
    // key 범위가 0x00 ~ 0xff니까 
    // 예) key길이가 2여서, 현재 streams는 streams[0], streams[1]까지 존재합니다.
    // streams[0] : I o m b z v ! l n   --> distribution값은 0
    // streams[1] : g m # p q l u s g   --> distribution값은 0이다.
    // 이제 각 streams에서 distribution값을 구해냅니다.

    // key_length = 2, input_length = 15
    for(int i = 0; i < key_length; i++){
        for(int j = 0; j < input_length / key_length; j++){
            for(int k = j+1; k < input_length / key_length ;k++){
                if(streams[i][k] == -1)                     //이미 중복된 문자는 계산을 해서 fraction와 합셈을 하고 빵꾸 난 부분을 -1로 채움
                    continue;
                if(streams[i][j] == streams[i][k]){
                    overlap++;
                    streams[i][k] = -1;
                }
            }
            fraction = overlap * (overlap-1);
            overlap=0;
        }
        distribution[i] = fraction / numerator;
        fraction = 0;
    }
    printf("\n");
    return 0;
}



int main(int argc, char* argv[]){
    FILE* fp = fopen(argv[1], "r");
    FILE* fp2 = fopen("hw1_output.txt", "w");

    char key_length=3;
    float temp_frequency=0.0;
    int buffer_length;
    fread(buffer, 1, MAX, fp);
    printf("%s\n",buffer);

    buffer_length = strlen(buffer);
    fclose(fp);

    //while(1){
        temp_frequency = find_frequency(key_length, buffer_length);
        key_length++;
        
    //}


    return 0;
}