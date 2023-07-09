import pymeshlab

def file_converter(input_file, output_file):
    # Create a MeshSet object
    mesh = pymeshlab.MeshSet()

    # Load the input FBX file
    mesh.load_new_mesh(input_file)

    # Export the mesh to SAT format
    mesh.save_current_mesh(output_file, save_vertex_color=True)

# Specify the input FBX file and output SAT file
input_file = "model/input.fbx"
output_file = "model/output.obj"


# Call the function to convert the files
file_converter(input_file, output_file)

