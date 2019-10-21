def coords2display(p,
                   valbounds=[-46.702880859375, -23.569022144054955, \
                              -46.69189453125, -23.57405696664267],
                   imgsize=[512, 256]):
    pnormalized = [(p[0] - valbounds[0]) / (valbounds[2]-valbounds[0]),
                   (p[1] - valbounds[1]) / (valbounds[3]-valbounds[1])]
    pnew = [ pnormalized[0]*imgsize[0], pnormalized[1]*imgsize[1] ]
    return pnew
