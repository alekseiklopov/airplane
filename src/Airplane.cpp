#include <cmath>

template <typename T>
struct Airplane
{
  Airplane(T x = 0, T y = 0, T v = 1, T theta = 1)
  : x(x), y(y), v(v), theta(theta)
  {
    this->set_constants();
  }

  void set_constants(T timestep = 0.001, T rho = 0.125, T m = 100, T F = 20,
    T Cx = 0.04, T Cy = 0.2, T g = 9.8)
  {
    this->timestep = timestep;
    this->rho = rho;
    this->m = m;
    this->F = F;
    this->Cx = Cx;
    this->Cy = Cy;
    this->g = g;
    this->t = 0;
  }

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

  T get_x()
  {
    return this->x;
  }

  T get_y()
  {
    return this->y;
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
    T x = this->x;
    T y = this->y;

    T v_next = v - g * sin(theta) * timestep -
      (rho * F * Cx * v * v * timestep) / (2 * m);
    T theta_next = theta - g * cos(theta) * timestep / v +
      (rho * F * Cy * v * timestep) / (2 * m);
    T x_next = x + v_next * cos(theta_next) * timestep;
    T y_next = y + v_next * sin(theta_next) * timestep;

    this->t += timestep;
    this->v = v_next;
    this->theta = theta_next;
    this->x = x_next;
    this->y = y_next;
  }

private:
  T x, y, v, theta, timestep, rho, m, F, Cx, Cy, t, g;
};
