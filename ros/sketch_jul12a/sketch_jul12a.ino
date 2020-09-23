#define STOP      0
#define FORWARD   1
#define BACKWARD  2
#define TURNLEFT  3
#define TURNRIGHT 4

int leftMotor1 =10 ;
int leftMotor2 =11 ;
int rightMotor1 =13 ;
int rightMotor2 =12 ;

int leftPWM = 5;
int rightPWM = 6;


int inputPin=7;   // 定义超声波信号接收接口
int outputPin=8;  // 定义超声波信号发出接口
int inputPin2=2;  // 定义第二个超声波信号接收接口
int outputPin2=4; // 定义第二个超声波信号发出接口

char val;

void setup() {
  // put your setup code here, to run once:
  //串口初始化
  Serial.begin(9600); 
  //测速引脚初始化
  pinMode(leftMotor1, OUTPUT);
  pinMode(leftMotor2, OUTPUT);
  pinMode(rightMotor1, OUTPUT);
  pinMode(rightMotor2, OUTPUT);
  pinMode(leftPWM, OUTPUT);
  pinMode(rightPWM, OUTPUT);
  //超声波控制引脚初始化
  pinMode(inputPin, INPUT);
  pinMode(outputPin, OUTPUT);
  pinMode(inputPin2, INPUT);
  pinMode(outputPin2, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  avoidance();
}
void motorRun(int cmd,int value)
{
  analogWrite(leftPWM, value);  //设置PWM输出，即设置速度
  analogWrite(rightPWM, value);
  switch(cmd){
    case FORWARD:
      Serial.println("FORWARD"); //输出状态
      digitalWrite(leftMotor1, HIGH);
      digitalWrite(leftMotor2, LOW);
      digitalWrite(rightMotor1, HIGH);
      digitalWrite(rightMotor2, LOW);
      break;
    case BACKWARD:
      Serial.println("BACKWARD"); //输出状态
      digitalWrite(leftMotor1, LOW);
      digitalWrite(leftMotor2, HIGH);
      digitalWrite(rightMotor1, LOW);
      digitalWrite(rightMotor2, HIGH);
      break;
     case TURNRIGHT:
      Serial.println("TURN  LEFT"); //输出状态
      digitalWrite(leftMotor1, HIGH);
      digitalWrite(leftMotor2, LOW);
      digitalWrite(rightMotor1, LOW);
      digitalWrite(rightMotor2, HIGH);
      break;
     case TURNLEFT:
      Serial.println("TURN  RIGHT"); //输出状态
      digitalWrite(leftMotor1, LOW);
      digitalWrite(leftMotor2, HIGH);
      digitalWrite(rightMotor1, HIGH);
      digitalWrite(rightMotor2, LOW);
      break;
     case STOP:
      Serial.println("STOP"); //输出状态
      digitalWrite(leftMotor1, LOW);
      digitalWrite(leftMotor2, LOW);
      digitalWrite(rightMotor1, LOW);
      digitalWrite(rightMotor2, LOW);
      break;
     
  }
}
void avoidance()
{
  int dis;//距离
  int dis2;//距离
  dis=getDistance(); //左边
  dis2=getDistance2(); //右边
  val=Serial.read();
  
  if(dis<=25&&dis2<=25)//直走
  {
    if(dis>5&&dis2>5)
    {
        /*motorRun(TURNRIGHT,250);
        delay(185);
        motorRun(FORWARD,300);
        delay(500);*/
        
      motorRun(FORWARD,400);
      delay(50);
    }
   //delay(500);
   }
  
   if(dis>=30&&dis2>=30)//停止并判断方向
  {
    motorRun(STOP,0);
    //motorRun(TURNLEFT,250);
    //转弯，树莓派识别箭头控制转弯
    delay(500);
    while(Serial.available())//左转
    {
      if(val == 'l')
      {
        Serial.println("left");
        motorRun(TURNLEFT,250);
        delay(210);
        motorRun(FORWARD,400);
        delay(500);
        motorRun(STOP,0);
        
       }
      //delay(500);
      
      if(val == 'r')
      {
        Serial.println("Right");
        motorRun(TURNRIGHT,250);
        delay(210);
        motorRun(FORWARD,400);
        delay(500);
        motorRun(STOP,0);
        
       }
      //delay(500);

      if(val =='s')
      {
        Serial.println("stop");
        motorRun(STOP,0);
        
       }
      delay(500);
    }
  }

 if(0<=dis&&dis<5)//让它走到中间
  {
    if(dis2<30&&dis2>25)
    {
      motorRun(TURNRIGHT,200);
      delay(100);
      motorRun(FORWARD,400);
      delay(100);
      motorRun(TURNLEFT,200);
      delay(100);
      motorRun(STOP,0);
    }
  }
  if(0<=dis2&&dis<5)//中间
  {
    if(dis<30&&dis>25)
    {
      motorRun(TURNLEFT,200);
      delay(100);
      motorRun(FORWARD,200);
      delay(100);
      motorRun(TURNRIGHT,200);
      delay(100);
      motorRun(STOP,0);
    }
  }

}
int getDistance()
{
  digitalWrite(outputPin, LOW); // 使发出发出超声波信号接口低电平2μs
  delayMicroseconds(2);
  digitalWrite(outputPin, HIGH); // 使发出发出超声波信号接口高电平10μs，这里是至少10μs
  delayMicroseconds(10);
  digitalWrite(outputPin, LOW); // 保持发出超声波信号接口低电平
  int distance = pulseIn(inputPin, HIGH); // 读出脉冲时间
  distance= distance/58; // 将脉冲时间转化为距离（单位：厘米）
  Serial.println(distance); //输出距离值
 
  if (distance >=50)
  {
    //如果距离小于50厘米返回数据
    return 50;
  }//如果距离小于50厘米小灯熄灭
  else
    return distance;
}

int getDistance2()
{
  digitalWrite(outputPin2, LOW); // 使发出发出超声波信号接口低电平2μs
  delayMicroseconds(2);
  digitalWrite(outputPin2, HIGH); // 使发出发出超声波信号接口高电平10μs，这里是至少10μs
  delayMicroseconds(10);
  digitalWrite(outputPin2, LOW); // 保持发出超声波信号接口低电平
  int distance2 = pulseIn(inputPin2, HIGH); // 读出脉冲时间
  distance2= distance2/58; // 将脉冲时间转化为距离（单位：厘米）
  Serial.println(distance2); //输出距离值
 
  if (distance2 >=50)
  {
    //如果距离小于50厘米返回数据
    return 50;
  }//如果距离小于50厘米小灯熄灭
  else
    return distance2;
} 
