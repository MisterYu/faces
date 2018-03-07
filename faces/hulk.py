import numpy as np


# TODO: do background vs face discrimination
def angry(face):
    # convert to float and normalize
    face_float = face.astype(float)
    face_norm = face_float/face_float.max()

    # scale normalized face to hulk green
    hulk_green = [21, 130, 2]
    temp = ((hulk_green[i]*face_norm).astype(np.uint8) for i in range(3))
    hulk_face = np.stack(temp, -1)

    return hulk_face
