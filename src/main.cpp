#include <iostream>
#include <cmath>
#include "Airplane.cpp"
#include <unistd.h>


int main()
{
  Airplane<double> airplane = Airplane<double>(0, 1000, 20, 3.14*6/180);

  for (int i = 0; i != 1000; ++i)
  {
    if (airplane.get_y() < 0)
    {
      break;
    }
    std::cout <<
    "Time=" << airplane.get_t() << "; " <<
    "v=" << airplane.get_v() << "; " <<
    "theta=" << airplane.get_theta() * 180 / 3.14 << "; " <<
    "x=" << airplane.get_x() << "; " <<
    "y=" << airplane.get_y() <<
    std::endl;
    airplane.do_time_step();
    usleep(100000);
  }

  return 0;
}
