import pygame, unittest, os, test_utils
from pygame.locals import *

CUBE_POINTS = (
    (0.5, -0.5, -0.5),  (0.5, 0.5, -0.5),
    (-0.5, 0.5, -0.5),  (-0.5, -0.5, -0.5),
    (0.5, -0.5, 0.5),   (0.5, 0.5, 0.5),
    (-0.5, -0.5, 0.5),  (-0.5, 0.5, 0.5)
)

CUBE_QUAD_VERTS = (
    (0, 1, 2, 3), (3, 2, 7, 6), (6, 7, 5, 4),
    (4, 5, 1, 0), (1, 5, 7, 2), (4, 0, 3, 6)
)


class GL_ImageSave(unittest.TestCase):
    def test_image_save_works_with_opengl_surfaces(self):
        #pygame.init()
        from OpenGL.GL import *
        from OpenGL.GLU import *
        screen = pygame.display.set_mode((640,480), OPENGL|DOUBLEBUF)

        glBegin(GL_QUADS)
        for face in CUBE_QUAD_VERTS:
            for vert in face:
                glVertex3fv(CUBE_POINTS[vert])
        glEnd()


        pygame.display.flip()

        tmp_dir = test_utils.get_tmp_dir()
        tmp_file = os.path.join(tmp_dir, "opengl_save_surface_test.png")

        pygame.image.save(screen, tmp_file)

        self.assert_(os.path.exists(tmp_file))

        os.remove(tmp_file)


if __name__ == '__main__': 
    unittest.main()