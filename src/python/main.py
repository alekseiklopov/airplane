import os
# from math import cos, sin, pi

import pychrono.core as chrono
import pychrono.irrlicht as chronoirr

from Glider import Glider


def model():
    dir_path = os.path.dirname(os.path.realpath(__file__)) + "/data/"

    chrono.SetChronoDataPath(dir_path)
    system = chrono.ChSystemNSC()

    chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.001)
    chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.001)

    k_coord = 500
    glider = Glider(0, 1000, 20, 3.14 * 6 / 180)

    glider_model = chrono.ChBodyEasyMesh(chrono.GetChronoDataFile('glider.obj'), 8000, True, True)
    glider_model.SetPos(chrono.ChVectorD(glider.get_x() / k_coord, glider.get_y() / k_coord, 0))
    # glider_model.SetRot(chrono.ChMatrix33D(glider.get_theta(), chrono.ChVectorD(0, 0, 1)))

    glider_model.SetBodyFixed(True)
    glider_model.SetName("glider")
    system.Add(glider_model)

    app = chronoirr.ChIrrApp(system, 'Glider modeling', chronoirr.dimension2du(800, 600))
    app.AddTypicalSky()
    app.AddTypicalCamera(chronoirr.vector3df(0, 0, -10), chronoirr.vector3df(0, 0, 0))
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
        # glider_model.SetRot(chrono.ChMatrix33D(glider.get_theta(), chrono.ChVectorD(0, 0, 1)))
        # glider_model.SetRot(chrono.ChQuaternionD(1, 0, 0, 0))
        # print(glider_model.GetRot())
        # glider_model.SetRot(chrono.ChQuaternionD(0.526892, 0.472112, -0.52567, 0.472405*sin(glider.get_theta()/2)))
        app.BeginScene()
        app.DrawAll()
        app.DoStep()
        app.EndScene()


if __name__ == "__main__":
    model()
