#--A fork of maoiscat's "mvtools_3.py" featured in the awesome-mpv script compilation and nand's original "mvtools.vpy" scripts.
#--This script retains the integrity of the frame rate conversion option found in the original script while using maoiscat's logical operations.
#--I've commented out code with a hashtag and two hyphens so my comments don't pass through the compiler.
import vapoursynth as vs
core = vs.core
clip = video_in.resize.Bicubic(format=vs.YUV420P8)
vden = 1000
vfps = container_fps*vden
dfps = display_fps*vden

#--Skip frame rate conversion for >4K or >240fps content due to gpu bottleneck. ※Note: The spaces serving as indentation are imperative for the correct functionality of this script; replacing the spaces with indents will break it.
if not (clip.width > 3000 or clip.height > 2000 or container_fps > 240):
    vfps_num = int(container_fps * 1e8)
    vfps_den = int(1e8)
    dfps_num = int(dfps * 1e4)
    dfps_den = int(1e4)

    clip = core.std.AssumeFPS(clip, fpsnum=vfps, fpsden=vden)
    print("Reflowing from ",vfps/vden," fps to ",dfps_num/dfps_den," fps.")
    super = core.mv.Super(clip, pel=2, sharp=0, rfilter=2)
    mvfw = core.mv.Analyse(super, blksize=32, isb=False, search=3, dct=5)
    mvbw = core.mv.Analyse(super, blksize=32, isb=True,  search=3, dct=5)
    clip = core.mv.FlowFPS(clip, super, mvbw, mvfw, num=dfps, den=vden, mask=1)

clip.set_output()
