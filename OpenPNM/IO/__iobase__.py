# -*- coding: utf-8 -*-
import OpenPNM
import scipy as sp
import scipy.sparse as sprs
import numpy as np

class NetToVtp(OpenPNM.BAS.OpenPNMbase):
    r"""
    NetToVtp - Export a network as VTK VTP file
    
    This class exports a pore newtork as a VTK file.
    
    Parameters
    ----------
    
    net : OpenPNM.NET.GenericNetwork
        Pore network
    filename : sring
        Filename
    
        
    Attributes
    ----------
    
     
            
    Examples
    --------
    
    Create and store a basic network.
    >>> import OpenPNM as PNM
    >>> net = PNM.GEN.SimpleCubic(divisions = [40,40,20],shape=[0.,4.,0.,4.,0.,2.]).generate()
    >>> PNM.IO.
    
    """
    
    def __init__(self,net = None, filename = 'testvtp.vtp'):
        super(NetToVtp,self).__init__()
        
        self._f = open(filename,'w')
        self._net=net
        
        self.write_vtk_header()
        self.write_vtk_points()
        self.write_vtk_connections()
        self.write_point_data()
        #self.write_edge_data()
        self.write_footer()
        self._f.close()
        
    def write_vtk_header(self):
        self._f.write('<?xml version="1.0"?>\n')
        self._f.write('<VTKFile type="PolyData" version="0.1" byte_order="LittleEndian">\n')
        self._f.write('<PolyData>\n')
        self._f.write('<Piece NumberOfPoints="')
        #text = str(pn.getNumPores())
        self._f.write(str(self._net.get_num_pores()))
        self._f.write('" NumberOfVerts="0" NumberOfLines="')
        #text = str(pn.getNumThroats())
        self._f.write(str(self._net.get_num_throats()))
        self._f.write('" NumberOfStrips="0" NumberOfPolys="0">\n')
    
    def write_vtk_points(self):
        self._f.write('<Points>\n')
        self._f.write('<DataArray type="Float32" NumberOfComponents="3" format="ascii">\n')
        for i in range(self._net.get_num_pores()):
            self._f.write(str(self._net.pore_properties['coords'][i,0]))
            self._f.write(' ')
            self._f.write(str(self._net.pore_properties['coords'][i,1]))
            self._f.write(' ')
            self._f.write(str(self._net.pore_properties['coords'][i,2]))
            self._f.write('\n')
        self._f.write('\n</DataArray>\n</Points>\n')
    
    def write_vtk_connections(self):
        self._f.write('<Lines>\n<DataArray type="Int32" Name="connectivity" format="ascii">\n')
        for i in range(self._net.get_num_throats()):
            self._f.write(str(self._net.throat_properties['connections'][i,0]))
            self._f.write(' ')
            self._f.write(str(self._net.throat_properties['connections'][i,1]))
            self._f.write(' ')
        self._f.write('\n</DataArray>\n<DataArray type="Int32" Name="offsets" format="ascii">\n')
        for i in range(self._net.get_num_throats()):
            self._f.write(str((i+1)*2))
            self._f.write(' ')            
        self._f.write('\n</DataArray>\n</Lines>\n')
    
    def write_point_data(self):
        pore_keys = self._net.pore_properties.keys()
        num_pore_keys = sp.size(pore_keys)
        self._f.write('<PointData Scalars="pore_data">\n')
        for j in range(num_pore_keys):
            if pore_keys[j] !='coords':
                self._f.write('<DataArray type="Float32" Name="')
                self._f.write(pore_keys[j])
                self._f.write('" format="ascii">\n')
                shape =  np.shape(self._net.pore_properties[pore_keys[j]])
                if np.size(shape) == 1:
                    for i in range(self._net.get_num_pores()):
                        self._f.write(str(self._net.pore_properties[pore_keys[j]][i]))
                        self._f.write(' ')
                else:
                    for i in range(self._net.get_num_pores()):
                        self._f.write(str(self._net.pore_properties[pore_keys[j]][i][0]))
                        self._f.write(' ')
                self._f.write('\n</DataArray>\n')
        self._f.write('</PointData>\n')
        
    def write_footer(self):
        self._f.write('</Piece>\n</PolyData>\n</VTKFile>')
                
        
class NetToVtp2(NetToVtp):
    
    def __init__(self,net = None, filename = 'testvtp.vtp'):
        super(NetToVtp2,self).__init__(net = None, filename = 'testvtp.vtp')
        
    def write_vtk_header(self):
        self._f.write('<?xml version="1.0"?>\n')
        self._f.write('<VTKFile type="PolyData" version="0.1" byte_order="LittleEndian">\n')
        self._f.write('<PolyData>\n')
        self._f.write('<Piece NumberOfPoints="')
        #text = str(pn.getNumPores())
        self._f.write(str(self._net.get_num_pores()))
        self._f.write('" NumberOfVerts="0" NumberOfLines="')
        #text = str(pn.getNumThroats())
        self._f.write(str(self._net.get_num_throats()))
        self._f.write('" NumberOfStrips="0" NumberOfPolys="0">\n')        
        
    