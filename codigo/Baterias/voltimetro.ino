void setup() {
    Serial.begin(9600);   
}
#define N 100
#define v "1.4.11"

void loop(){
    if(Serial.available()>0){
        while(Serial.available() ) Serial.read();
        float media = 0;
            for(int i = 0 ; i < N ; i++ ){
            int value = analogRead(A0);
            int v33 = analogRead(A1) ;  // 3.3 = cte * v33 / 1023 so cte = 3.3 * 1023 / v33
            float voltios = value  * 3.3 /v33 ; // voltios = value * 3.3 * 1023 / ( 1023 * v33 )
            media += voltios;
            delay(10);   
        }
        Serial.println(media / N);
    }
}