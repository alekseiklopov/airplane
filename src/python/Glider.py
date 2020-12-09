from math import sin, cos


class Glider:
    def __init__(self, x, y, v, theta):
        self.x = x
        self.y = y
        self.v = v
        self.theta = theta
        self.timestep = 0.001
        self.rho = 0.125
        self.m = 100
        self.F = 20
        self.Cx = 0.04
        self.Cy = 0.2
        self.t = 0
        self.g = 9.8

    # def set_contants(self, timestep, rho, m, F, Cx, Cy, g):
    #     self.timestep = timestep
    #     self.rho = rho
    #     self.m = m
    #     self.F = F
    #     self.Cx = Cx
    #     self.Cy = Cy
    #     self.t = 0
    #     self.g = g

    def get_t(self):
        return self.t

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_v(self):
        return self.v

    def get_theta(self):
        return self.theta

    def do_timestep(self):
        v_next = self.v - self.g * sin(self.theta) * self.timestep - \
                 (self.rho * self.F * self.Cx * pow(self.v, 2) * self.timestep) / (2 * self.m)
        theta_next = self.theta - self.g * cos(self.theta) * self.timestep / self.v + \
                     (self.rho * self.F * self.Cy * self.v * self.timestep) / (2 * self.m)
        x_next = self.x + v_next * cos(theta_next) * self.timestep
        y_next = self.y + v_next * sin(theta_next) * self.timestep

        self.t += self.timestep
        self.v = v_next
        self.theta = theta_next
        self.x = x_next
        self.y = y_next

    def print_state(self):
        print("t={:.1f}, x={:.1f}, y={:.1f}, v={:.1f}, theta={:.1f}"
              .format(self.t, self.x, self.y, self.v, self.theta * 180 / 3.14))
