@alg(name="vertical_reflection", label="Vertical Reflection",
     group="examplescripts", group_label="Example scripts")
@alg.input(type=alg.SOURCE, name="INPUT", label="Input vector layer")
@alg.input(type=alg.DISTANCE, name="AXIS", label="Reflection axis X-coordinate")
@alg.input(type=alg.VECTOR_LAYER_DEST, name="OUTPUT_PATH", label="Output path")
@alg.output(type=alg.FILE, name="OUTPUT", label="Reflected geometries")

def vertical_reflection(instance, parameters, context, feedback, inputs):
    """
    Tworzy odbicie pionowe geometrii względem podanej wartości X.
    """
    layer = instance.parameterAsVectorLayer(parameters, "INPUT", context)
    axis_x = instance.parameterAsDouble(parameters, "AXIS", context)
    output_path = instance.parameterAsOutputLayer(parameters, "OUTPUT_PATH", context)
    crs = layer.crs().authid()
    reflected_layer = QgsVectorLayer("Polygon?crs=" + crs, "Reflected", "memory")
    if feedback.isCanceled():
        return {}
    features = []
    for feature in layer.getFeatures():
        geom = feature.geometry()
        geom_type = geom.type()
        vertices = geom.vertices()
        reflected_vertices = []
        for vertex in vertices:
            new_x = 2 * axis_x - vertex.x()
            new_y = vertex.y()
            reflected_vertices.append(QgsPointXY(new_x, new_y))
        if geom_type == 0:
            new_geom = QgsGeometry.fromPointXY(reflected_vertices[0])
        elif geom_type == 1:
            new_geom = QgsGeometry.fromPolylineXY(reflected_vertices)
        elif geom_type == 2:
            new_geom = QgsGeometry.fromPolygonXY([reflected_vertices])
        reflected_feature = QgsFeature()
        reflected_feature.setGeometry(new_geom)
        features.append(reflected_feature)
    reflected_layer.dataProvider().addFeatures(features)
    reflected_layer.updateExtents()
    if feedback.isCanceled():
        return {}
    QgsVectorFileWriter.writeAsVectorFormatV3(
        layer=reflected_layer,
        fileName=output_path,
        transformContext=context.transformContext(),
        options=QgsVectorFileWriter.SaveVectorOptions()
    )
    return {"OUTPUT": output_path}

