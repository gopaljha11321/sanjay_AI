
#include<Servo.h>

Servo head;
Servo l_hand;
Servo r_hand;
int po=0;

// define sonar sensor's pins
int trig = 9;
int echo = 8;

// received data
byte val = "";

void setup() {
  // put your setup code here, to run once:
  head.attach(10);
  l_hand.attach(12);
  r_hand.attach(11);

  Serial.begin(9600); 
  // for communicating via serial port with Python
}

void standby(){
  head.write(0);
  
  l_hand.write(30);
  r_hand.write(30);
  return;
}

void hi(){
  // all motors to these positions

  int i = 0;
  for(i=30; i<= 170; i++){
    r_hand.write(i);
    delay(5);
  }

  for(i=170; i>= 100; i--){
    r_hand.write(i);
    delay(5);
  }

  for(i=100; i<= 170; i++){
    r_hand.write(i);
    delay(5);
  }

  for(i=170; i>= 30; i--){
    r_hand.write(i);
    delay(5);
  }

  standby();
}

void hands_up(){
  head.write(0);
  delay(20);
   for (po = 0; po <= 150; po += 1){
    delay(10);
  head.write(po);
  }
  for(po = 150; po>=0; po -=1){
    head.write(po);              // tell servo to go to position in variable 'pos'
    delay(10);
    }
  int i;
  for(i=30; i<= 170; i++){
    int l_pos = map(i, 0, 180, 180, 0);
  
    l_hand.write(l_pos);
    r_hand.write(i);
    r_hand.write(0);
    delay(5);
  }

  delay(60);

  for(i=170; i>= 30; i--){
    int r_pos = i;
    int l_pos = map(r_pos, 0, 180, 180, 0);
  
    l_hand.write(l_pos);
    r_hand.write(r_pos);
    delay(5);
  }
  
}

void weight_lift(){
  // lift weight using both hands
  int i = 0;
  for(i=30; i<= 170; i++){
    int r_pos = i;
    int l_pos = map(r_pos, 0, 180, 180, 0);
  
    l_hand.write(l_pos);
    r_hand.write(r_pos);
    delay(5);
  }

  for(int count=0; count<=4; count++){
    for(i=170; i>= 60; i--){
      int r_pos = i;
      int l_pos = map(r_pos, 0, 180, 180, 0);
  
      l_hand.write(l_pos);
      r_hand.write(r_pos);
      delay(5);
      }

    for(i=60; i<= 170; i++){
      int r_pos = i;
      int l_pos = map(r_pos, 0, 180, 180, 0);
  
      l_hand.write(l_pos);
      r_hand.write(r_pos);
      delay(5);
      }
    }

  for(i=170; i>= 30; i--){
    int r_pos = i;
    int l_pos = map(r_pos, 0, 180, 180, 0);
  
    l_hand.write(l_pos);
    r_hand.write(r_pos);
    delay(5);
  }
}

void excited(){
  return;
}

void look_left(){
  // rotate hed to left
  head.write(180);
}

void confused(){

  for(int count=0; count<=1; count++){
    head.write(30);
    r_hand.write(170);
    delay(700);
    r_hand.write(30);
    head.write(120);
    l_hand.write(30);
    delay(700);
    l_hand.write(160);
    }
  standby();
}

void double_punch(){
  // do a punch
  int i = 0;
  for(i=30; i>= 0; i--){
      int r_pos = i;
      int l_pos = map(r_pos, 0, 180, 180, 0);
  
      l_hand.write(l_pos);
      r_hand.write(r_pos);
      delay(5);
      }
  delay(2000);
  
  int r_pos = 80;
  int l_pos = map(r_pos, 0, 180, 180, 0);
  l_hand.write(l_pos);
  r_hand.write(r_pos);
  delay(500);
  standby();
}

void r_upper_cut(){
  // make right upper-cut
  int i = 0;
  for(i=30; i<= 170; i++){
    int r_pos = i;
    int l_pos = map(r_pos, 0, 180, 180, 0);
  
    l_hand.write(l_pos);
    r_hand.write(r_pos);
    delay(5);
  }

  for(int count=0; count<=4; count++){
    int i = 0;
    for(i=170; i>= 60; i--){
      r_hand.write(i);
      delay(1);
      }

    for(i=60; i<= 170; i++){
      r_hand.write(i);
      delay(1);
      }
    }
   standby();
   delay(100);
}

void smash(){
  // smash things
  int i = 0;
  for(i=30; i<= 170; i++){
    int r_pos = i;
    int l_pos = map(r_pos, 0, 180, 180, 0);
  
    l_hand.write(l_pos);
    r_hand.write(r_pos);
    delay(5);
  }
  delay(2000);
  for(i=170; i>= 0; i--){
    int r_pos = i;
    int l_pos = map(r_pos, 0, 180, 180, 0);
  
    l_hand.write(l_pos);
    r_hand.write(r_pos);
    delay(1);
  }
  delay(300);
  int r_pos = 180;
  int l_pos = map(r_pos, 0, 180, 180, 0);
  
  l_hand.write(l_pos);
  r_hand.write(r_pos);
  delay(1000);
  standby();
}

void eye_detect(){
  // do something if eye sensor detect motion
  return;
}
void rotate_head(){
  head.write(180);
  delay(500);
}
void rotate_hand(){
  
  r_hand.write(180);
  delay(500);
  
}


void loop() {
  // put your main code here, to run repeatedly:
  standby();
  
  while(Serial.available() > 0)  //look for serial data available or not
  {
    val = Serial.read();        //read the serial value

    if(val == 'h'){
      // do hi
       hi();
    }
    if(val == 'p'){
      // do hi
       double_punch();
    }
    if(val == 'u'){
      hands_up();
    }
    if(val == 'l'){
      standby();
      look_left();
      delay(2000);
    }
    if(val == 'U'){
      // uppercut
      r_upper_cut();
      delay(2000);
    }
    if(val == 's'){
      smash();
      delay(2000);
    }
    if(val == 'x'){
      rotate_head();
      delay(2000);
    }
    if(val== 'w'){
      rotate_hand();
      delay(2000);
    }
  }
}
