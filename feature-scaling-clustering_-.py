""" quiz materials for feature scaling clustering """

def featureScaling(arr):
    arr1 = list()
    arr_len = len(arr)
    arr0 = sorted(arr)
    arr_range = arr0[arr_len-1]-arr0[0]
    for a in arr0:
        arr1.append(float(a-arr0[0])/arr_range)
    return arr1

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)
