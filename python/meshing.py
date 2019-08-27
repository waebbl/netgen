from .libngpy._meshing import *

class _MeshsizeObject:
    @property
    def very_coarse(self):
        return MeshingParameters(curvaturesafety=1,
                                 segmentsperedge=0.3,
                                 grading=0.7,
                                 surfcurvfac=0.25,
                                 chartdistfac=0.8,
                                 linelengthfac=0.2,
                                 closeedgefac=0.5,
                                 minedgelen=0.002,
                                 edgeanglefac=0.25,
                                 surfmeshcurvfac=1.,
                                 optsteps3d=5)
    @property
    def coarse(self):
        return MeshingParameters(curvaturesafety=1.5,
                                 segmentsperedge=0.5,
                                 grading=0.5,
                                 surfcurvfac=0.5,
                                 chartdistfac=1,
                                 linelengthfac=0.35,
                                 closeedgefac=1,
                                 minedgelen=0.02,
                                 edgeanglefac=0.5,
                                 surfmeshcurvfac=1.5,
                                 optsteps3d=5)
    @property
    def moderate(self):
        return MeshingParameters(curvaturesafety=2,
                                 segmentsperedge=1,
                                 grading=0.3,
                                 surfcurvfac=1.,
                                 chartdistfac=1.5,
                                 linelengthfac=0.5,
                                 closeedgefac=2,
                                 minedgelen=0.2,
                                 edgeanglefac=1,
                                 surfmeshcurvfac=2.,
                                 optsteps3d=5)
    @property
    def fine(self):
        return MeshingParameters(curvaturesafety=3,
                                 segmentsperedge=2,
                                 grading=0.2,
                                 surfcurvfac=1.5,
                                 chartdistfac=2,
                                 linelengthfac=1.5,
                                 closeedgefac=3.5,
                                 minedgelen=1.,
                                 edgeanglefac=1.5,
                                 surfmeshcurvfac=3.,
                                 optsteps3d=5)

    @property
    def very_fine(self):
        return  MeshingParameters(curvaturesafety=5,
                                  segmentsperedge=3,
                                  grading=0.1,
                                  surfcurvfac=3,
                                  chartdistfac=5,
                                  linelengthfac=3,
                                  closeedgefac=5,
                                  minedgelen=2.,
                                  edgeanglefac=3.,
                                  surfmeshcurvfac=5.,
                                  optsteps3d=5)

meshsize = _MeshsizeObject()
