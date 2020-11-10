import vapoursynth as vs
core = vs.core
clip = video_in
vden = 1000
vfps = int(container_fps*vden)
dden = 1000
dfps = int(display_fps*dden)
#For YUV420P10 better to uncomment the next line for better performance
#clip = core.resize.Bicubic(clip, format=vs.YUV420P8)
clip = core.std.AssumeFPS(clip, fpsnum=vfps, fpsden=vden)
super = core.mv.Super(clip, pel=2, sharp=0, rfilter=2, hpad=8, vpad=8, levels=0)
mvfw = core.mv.Analyse(super, blksize=64, overlap=32, isb=False, search=4, searchparam=6, pelsearch=3)
mvbw = core.mv.Analyse(super, blksize=64, overlap=32, isb=True,  search=4, searchparam=6, pelsearch=3)
clip = core.mv.BlockFPS(clip, super, mvbw, mvfw, num=dfps, den=dden)
clip.set_output()
