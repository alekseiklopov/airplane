#include <cmath>

template <typename T>
struct Airplane
{
  Airplane(T v_0 = 1, T theta_0 = 0.5, T timestep = 1,
    T rho = 1.225, T m = 10, T F = 1,
    T Cx = 0.058, T Cy = 0.58)
  : t(0), v(v_0), theta(theta_0), timestep(timestep), g(9.8),
    rho(rho), m(m), F(F), Cx(Cx), Cy(Cy)
  {}

  T get_t()
  {
    return this->t;
  }

  T get_v()
  {
    return this->v;
  }

  T get_theta()
  {
    return this->theta;
  }

  void do_time_step()
  {
    T v = this->v;
    T theta = this->theta;
    T timestep = this->timestep;
    T g = this->g;
    T Cx = this->Cx;
    T Cy = this->Cy;
    T m = this->m;
    T F = this->F;
    T rho = this->rho;
    T v_next = v - g * sin(theta) * timestep -
      (rho * F * Cx * v * v * timestep) / (2 * m);
    T theta_next = theta - g * cos(theta) * timestep / v +
      (rho * F * Cy * v * timestep) / (2 * m);
    this->t += timestep;
    this->v = v_next;
    this->theta = theta_next;
  }

private:
  T v, theta, timestep, rho, m, F, Cx, Cy, t, g;
};
