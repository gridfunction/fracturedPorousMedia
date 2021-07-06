from netgen.meshing import *
# only work with 3D gmsh files
def ReadGmsh(filename):
    if not filename.endswith(".msh"):
        filename += ".msh"
    meshdim = 3
    with open(filename, 'r') as f:
        while f.readline().split()[0] != "$Entities":
            pass
        line = f.readline().split()
        nverts = line[0]
        nlines = line[1]
        nfaces = line[2]
        ncells = line[3]
    
    f = open(filename, 'r')
    mesh = Mesh(dim=meshdim)
    
    pointmap = {} # mapping between netgen ordering and gmsh ordering
    facedescriptormap = {}

    namemap = {}
    vertmap = {}
    edgemap = {}
    facemap = {}
    cellmap = {}

    segm = 1
    trig = 2
    quad = 3
    tet = 4
    hex = 5
    prism = 6
    pyramid = 7
    segm3 = 8      # 2nd order line
    trig6 = 9      # 2nd order trig
    tet10 = 11     # 2nd order tet
    point = 15
    quad8 = 16     # 2nd order quad
    hex20 = 17     # 2nd order hex
    prism15 = 18   # 2nd order prism
    pyramid13 = 19 # 2nd order pyramid
    segms = [segm, segm3]
    trigs = [trig, trig6]
    quads = [quad, quad8]
    tets = [tet, tet10]
    hexes = [hex, hex20]
    prisms = [prism, prism15]
    pyramids = [pyramid, pyramid13]
    elem0d = [point]
    elem1d = segms
    elem2d = trigs + quads
    elem3d = tets + hexes + prisms + pyramids

    num_nodes_map = { segm : 2,
                      trig : 3,
                      quad : 4,
                      tet : 4,
                      hex : 8,
                      prism : 6,
                      pyramid : 5,
                      segm3 : 3,
                      trig6 : 6,
                      tet10 : 10,
                      point : 1,
                      quad8 : 8,
                      hex20 : 20,
                      prism15 : 18,
                      pyramid13 : 19 }

    while True:
        line = f.readline()
        if line == "":
            break
        
        # physical name maps
        if line.split()[0] == "$PhysicalNames":
            numnames = int(f.readline())
            for i in range(numnames):
                #f.readline
                line = f.readline()
                namemap[int(line.split()[1])] = line.split()[2][1:-1]
        
        # entities
        if line.split()[0] == "$Entities":
            line = f.readline()
            nP = int(line.split()[0])
            nE = int(line.split()[1])
            nF = int(line.split()[2])
            nC = int(line.split()[3])
            # points
            for i in range(nP):
                line = f.readline()
                pTag = int(line.split()[0])
                numP = int(line.split()[4])
                if numP ==1: # one point tag
                    vertmap[pTag] = namemap[int(line.split()[5])]
            # edges
            for i in range(nE):
                line = f.readline()
                eTag = int(line.split()[0])
                numE = int(line.split()[7])
                if numE ==1: # one point tag
                    edgemap[eTag] = namemap[int(line.split()[8])]
            # faces
            for i in range(nF):
                line = f.readline()
                fTag = int(line.split() [0])
                numF = int(line.split() [7])
                if numF ==1: # one point tag
                    facemap[fTag] = namemap[int(line.split() [8])]
            # cells
            for i in range(nC):
                line = f.readline()
                cTag = int(line.split()[0])
                numC = int(line.split()[7])
                if numC ==1: # one point tag
                    cellmap[cTag] = namemap[int(line.split()[8])]
        if line.split()[0] == "$Nodes":
            # number of nodes
            tmp = f.readline().split()
            numE = int(tmp[0]) # number of entity blocks
            numN = int(tmp[1]) # number of nodes
            for i in range(numE): # loop over blocks
                line1 = f.readline().split()
                eD = int(line1[0]) # entity dimesion
                eT = int(line1[1]) # entity tag
                nN = int(line1[-1]) # number of nodes in block
                
                nT = [] # node tag
                cT = [] # node coordinates 
                for i in range(nN):
                    nT.append(int(f.readline()))
                for i in range(nN):
                    tmp = f.readline().split()
                    cT.append(tmp[0:3])

                for i in range(nN):
                    nodenum = nT[i]
                    x, y, z = cT[i][0:3]
                    pnum = mesh.Add(MeshPoint(Pnt(float(x), float(y), float(z))))
                    pointmap[nodenum] = pnum
        
        index0, index1, index2, index3 = 0, 0, 0, 0
        if line.split()[0] == "$Elements":
            tmp = f.readline().split()
            nE = int(tmp[0]) # number of entity blocks
            numE = int(tmp[1]) # number of total elements
         
            for i in range(nE):
                line = f.readline().split()
                eD = int(line[0]) # entity dimension
                eT = int(line[1]) # entity tag
                elmtype = int(line[2]) # element type
                numE = int(line[3]) # number elements in block
                #print(eD, eT, elmtype, numE)

                if elmtype not in num_nodes_map:
                    raise Exception("element type", elmtype, "not implemented")
                num_nodes = num_nodes_map[elmtype]
                
                # CD3 :
                if elmtype in elem0d:
                    if eT in vertmap:
                        mesh.SetCD3Name(index0+1, vertmap[eT])
                    else:
                        mesh.SetCD3Name(index0+1, "point" + str(index0))
                    for i1 in range(numE):
                        tmp = f.readline().split()
                        nodenums = tmp[1:]
                        nodenums2 = [pointmap[int(nn)] for nn in nodenums]
                        mesh.Add(Element0D(nodenums2[0], index=index0))
                    index0 += 1
                    #stop

                # CD2 : FIXME later
                if elmtype in elem1d:
                    index1 += 1
                    if eT in edgemap:
                        mesh.SetCD2Name(index1, edgemap[eT])
                    else:
                        mesh.SetCD2Name(index1, "edge" + str(index1))
                    for i1 in range(numE):
                        tmp = f.readline().split()
                        nodenums = tmp[1:]
                        nodenums2 = [pointmap[int(nn)] for nn in nodenums]
                        mesh.Add(Element1D(index=index1, vertices=nodenums2))
                # CD1
                if elmtype in elem2d:  # 2d elements
                    index2 += 1
                    # add face descriptor
                    fd = FaceDescriptor(bc=index2)
                    if eT in facemap:
                        fd.bcname = facemap[eT]
                    else:
                        fd.bcname = 'surf' + str(index2)
                    mesh.SetBCName(index2-1, fd.bcname)
                    mesh.Add(fd)
                    
                    if elmtype in trigs:
                        ordering = [i for i in range(3)]
                        if elmtype == trig6:
                            ordering += [4,5,3]
                    if elmtype in quads:
                        ordering = [i for i in range(4)]
                        if elmtype == quad8:
                            ordering += [4, 6, 7, 5]
                    for i1 in range(numE):
                        tmp = f.readline().split()
                        nodenums = tmp[1:]
                        nodenums2 = [pointmap[int(nn)] for nn in nodenums]
                        mesh.Add(Element2D(index2, [nodenums2[i] for i in ordering]))
                
                # volume elements
                if elmtype in elem3d:  # volume elements
                    index3 += 1
                    if eT in cellmap:
                        mesh.SetMaterial(index3, cellmap[eT])
                    else:
                        mesh.SetMaterial(index3, "vol" + str(index3))
                    
                    if elmtype in tets:
                        ordering = [0,1,2,3]
                        if elmtype == tet10:
                            ordering += [4,6,7,5,9,8]
                    elif elmtype in hexes:
                        ordering = [0,1,5,4,3,2,6,7]
                        if elmtype == hex20:
                            ordering += [8,16,10,12,13,19,15,14,9,11,18,17]
                    elif elmtype in prisms:
                        ordering = [0,2,1,3,5,4]
                        if elmtype == prism15:
                            ordering += [7,6,9,8,11,10,13,12,14]
                    elif elmtype in pyramids:
                        ordering = [3,2,1,0,4]
                        if elmtype == pyramid13:
                            ordering += [10,5,6,8,12,11,9,7]
                    for i1 in range(numE):
                        tmp = f.readline().split()
                        nodenums = tmp[1:]
                        nodenums2 = [pointmap[int(nn)] for nn in nodenums]
                        mesh.Add(Element3D(index3, [nodenums2[i] for i in ordering]))
    
    return mesh
