#include <iostream>
#include <cmath>
#include "Airplane.cpp"
#include <unistd.h>


int main()
{
  Airplane<double> airplane = Airplane<double>(0, 0, 1, 3.14*1/180);

  for (int i = 0; i != 1000; ++i)
  {
    std::cout <<
    "Time=" << airplane.get_t() << "; " <<
    "v=" << airplane.get_v() << "; " <<
    "theta=" << airplane.get_theta() * 180 / 3.14 << "; " <<
    "x=" << airplane.get_x() << "; " <<
    "y=" << airplane.get_y() << "; " <<
    std::endl;
    airplane.do_time_step();
    usleep(100000);
  }

  return 0;
}
