#include <iostream>
#include <cmath>
#include "Airplane.cpp"
#include <unistd.h>


int main()
{
  double v_0 = 1;
  double theta_0 = 3.14 * 1 / 180;
  double timestep = 0.1;
  Airplane<double> airplane = Airplane<double>(v_0=v_0, theta_0=theta_0, timestep=timestep);

  for (int i = 0; i != 100; ++i)
  {
    std::cout <<
    "Time=" << airplane.get_t() << "; " <<
    "v=" << airplane.get_v() << "; " <<
    "theta=" << airplane.get_theta() * 180 / 3.14 <<
    std::endl;
    airplane.do_time_step();
    sleep(1);
  }

  return 0;
}
