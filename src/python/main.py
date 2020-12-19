import os

import pychrono.core as chrono
import pychrono.irrlicht as chronoirr

from Glider import Glider

DEG_TO_RAD = 3.14159 / 180


def model():
    dir_path = os.path.dirname(os.path.realpath(__file__)) + "/data/"

    chrono.SetChronoDataPath(dir_path)
    system = chrono.ChSystemNSC()

    chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.001)
    chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.001)

    k_coord = 1  # scale coefficient
    x = 0        # initial coordinate, m
    y = 10       # initial coordinate, m
    v = 5        # initial velocity, m/s
    theta = 20   # initial angle, deg
    glider = Glider(x, y, v, theta * DEG_TO_RAD)

    glider_model = chrono.ChBodyEasyMesh(chrono.GetChronoDataFile('glider.obj'), 8000, True, True)
    glider_model.SetPos(chrono.ChVectorD(glider.get_x() / k_coord, glider.get_y() / k_coord, 0))
    glider_model.SetRot(chrono.ChQuaternionD(0.526892, 0.472112, -0.52567, 0.472405) *
                        chrono.Q_from_AngX(glider.get_theta() * DEG_TO_RAD))
    glider_model.SetBodyFixed(True)
    glider_model.SetName("glider")
    system.Add(glider_model)

    app = chronoirr.ChIrrApp(system, 'Glider modeling', chronoirr.dimension2du(800, 600))
    app.AddTypicalSky()
    app.AddTypicalCamera(chronoirr.vector3df(30, 10, -10), chronoirr.vector3df(0, 0, 0))
    app.AddLightWithShadow(chronoirr.vector3df(0, 100, 0), chronoirr.vector3df(0, 0, 0), 110, 1, 11, 100)
    app.AssetBindAll()
    app.AssetUpdateAll()
    app.AddShadowAll()
    app.SetTimestep(0.005)
    # app.SetTryRealtime(True)

    k = 0
    while app.GetDevice().run():
        if glider.get_y() < 0:
            break
        if k == 100:
            k = 0
            glider.print_state()
        k += 1
        glider.do_timestep()
        glider_model.SetPos(chrono.ChVectorD(glider.get_x() / k_coord, glider.get_y() / k_coord, 0))
        glider_model.SetRot(chrono.ChQuaternionD(0.526892, 0.472112, -0.52567, 0.472405) *
                            chrono.Q_from_AngX(glider.get_theta()))
        app.BeginScene()
        app.DrawAll()
        app.DoStep()
        app.EndScene()


if __name__ == "__main__":
    model()
