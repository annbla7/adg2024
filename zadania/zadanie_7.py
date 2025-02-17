vector.startEditing()

new_field = [QgsField("dlugosc_granicy", QVariant.Double)]
vector.dataProvider().addAttributes(new_field)
vector.updateFields()

len_index = vector.fields().indexOf("dlugosc_granicy")

for feature in vector.getFeatures():
    length = feature.geometry().length()
    length = length / 1000
    vector.changeAttributeValue(feature.id(), len_index, length)

vector.commitChanges()