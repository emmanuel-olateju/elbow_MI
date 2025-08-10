import numpy as np
import copy
from PIL import Image as im


def _a(data):
    return data/255.0

def _rs(data):
    return _a(data).reshape(-1,data.shape[0])

def _center(data):
    return data - np.mean(data,axis=0)

def _cov(data):
    return np.cov(data, rowvar=False)

def _eig(data):
    vals, vecs = np.linalg.eigh(_cov(data))

    sort_perm = vals[::-1].argsort()
    vals[::-1].sort()
    vecs = vecs[:, sort_perm]

    m1 = np.column_stack((vecs))

    return m1, vals, vecs

def pca(data, alpha_std):
    # data = im.fromarray(data)
    F,H,W=data.shape
    orig_img = copy.deepcopy(data)
    # data = _a(data)
    data = _rs(data)
    data = _center(data)
    m1, eig_vals, eig_vecs = _eig(data)
    alpha = np.random.normal(0, alpha_std)

    # for idx in range(F):
        # orig_img[idx,:,:] = np.matmul()
    #     orig_img = np.clip(orig_img, 0.0, 255.0)
        # orig_img = orig_img.astype(np.uint8)

    res_img = np.matmul(m1,_rs(orig_img).T)
    res_img=res_img.reshape(F,H,W)

    return res_img

def batch_pca(tensor):
    result=np.empty(tensor.shape)
    for i in range(tensor.shape[0]):
        result[i,:,:,:]=pca(tensor[i,:,:,:],0.1)
    return result

def fpca(data,alpha_std):
    F,H,W=data.shape
    orig_img = copy.deepcopy(data)
    data = _rs(data)
    data = _center(data)
    m1, eig_vals, eig_vecs = _eig(data)
    m2 = np.zeros((F,1))
    alpha = np.random.normal(0, alpha_std)

    m2[:, 0] = alpha * eig_vals[:]
    add_vect = np.matrix(m1) * np.matrix(m2)


    for h in range(H):
        for w in range(W):
            # print(orig_img[:,h,w].shape,add_vect.shape)
            orig_img[:,h,w] = orig_img[:,h,w] + add_vect.reshape(F)

    return orig_img

def batch_fpca(tensor,alpha):
    result=np.empty(tensor.shape)
    for i in range(tensor.shape[0]):
        result[i,:,:,:]=fpca(tensor[i,:,:,:],alpha)
    return result