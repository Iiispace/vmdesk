<div style="background-color: #909190; padding: 40px;">

# **Mesh Editor**

Mesh Editor used in **edit mode** for mesh objects.

![](./img/mesh_distance.png)

- **Distance**  
    Distance between 2 selected vertices  
    Unsigned Value

<br/>

- **Direction**  
    Direction of 2 selected vertices  
    Point to active vertex when attribute **"Invert"** is disabled

<br/>

- **Unit Vector**  
    Unit Direction

<br/>

![](./img/mesh_normal.png)

- **Normal**  
    Normal of 3 vertices or face
    - **Keep Normals to Other Faces**  
        Keep normals of unselected faces if possible
    - **Lock Active Vertex**  
        Keep active vertex location

<br/>

- **Vertex Limit**  
    Deactivate the property when the selected vertex count exceeds this value

<br/>

- **Collinear Threshold**  
    The smaller the value, the closer to collinear

<br/>

- **Coplanar Threshold**  
    The smaller the value, the closer to coplanar

<br/>

- **Make Collinear**  
    Make selected vertices collinear  
    - **Lock Active Vertex**  
        Keep active vertex location

<br/>

- **Make Coplanar**  
    Make selected vertices coplanar  
    - **Lock Active Vertex**  
        Keep active vertex location

<br/>

- **Area**  
    Total area of ​​selected faces
    - **Lock Active Vertex**  
        Keep active vertex location

<br/>

- **Included Angle**  
    Unsigned angle between 2 edges. If 3 vertices selected, the angle will be based on the second selected vertex.
    When modifying the angle, the last selected vertex will move and maintain the length from the second vertex
    - **Lock Active Vertex**  
        Keep active vertex location