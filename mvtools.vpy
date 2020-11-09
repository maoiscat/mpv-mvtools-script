import vapoursynth as vs
core = vs.core
clip = video_in
vden = 1000
vfps = int(container_fps*vden)
dden = 1000
dfps = int(display_fps*dden)
clip = core.std.AssumeFPS(clip, fpsnum=vfps, fpsden=vden)
super = core.mv.Super(clip, pel=2, sharp=0, rfilter=2, hpad=8, vpad=8, levels=0)
mvfw = core.mv.Analyse(super, blksize=64, isb=False, search=3, searchparam=3)
mvfw = core.mv.Recalculate(super, mvfw, blksize=16, search=3, searchparam=1, thsad=200)
mvbw = core.mv.Analyse(super, blksize=64, isb=True, search=3, searchparam=3)
mvbw = core.mv.Recalculate(super, mvbw, blksize=16, search=3, searchparam=1, thsad=200)
clip = core.mv.BlockFPS(clip,super,mvbw,mvfw,num=dfps,den=dden)
clip.set_output()