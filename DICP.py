import numpy as np
from sklearn.preprocessing import MinMaxScaler

import COLORS


class getDICPInfo:
    def __init__(self, dataframe, class_count, feature_count, sample_count,
                 count_per_class_array):

        # dataset information
        self.dataframe = dataframe
        self.class_count = class_count
        self.feature_count = feature_count
        self.sample_count = sample_count
        self.count_per_class_array = count_per_class_array

    def getClassVertices(self):
        df = self.dataframe.copy()

        for i in range(2, self.feature_count):
            df[df.columns[i]] += df[df.columns[i - 2]]

        # scale attributes to fit to graphic coordinate system -0.8 to 0.8
        scaler = MinMaxScaler((-0.8, 0.8))
        tmp = df.to_numpy().reshape(-1, 1)
        scaled = scaler.fit_transform(tmp).reshape(len(df), self.feature_count)
        df.loc[:] = scaled

        # get xy_coord [[0,0],[2,0]]
        xy_coord = df.to_numpy()
        xy_coord = xy_coord.ravel()
        xy_coord = np.reshape(xy_coord, (-1, 2))

        # how to randomly generate more colors?
        colors = COLORS.getColors()
        class_color_array = colors.colors_array

        color_array = np.tile(class_color_array[0], reps=(self.count_per_class_array[0] * int((self.feature_count / 2)), 1))
        for i in range(1, self.class_count):
            temp_array = np.tile(class_color_array[i], reps=(self.count_per_class_array[i] * int((self.feature_count / 2)), 1))
            color_array = np.concatenate((color_array, temp_array))

        data_plot_indices = np.arange(0, self.sample_count * int(self.feature_count / 2), int(self.feature_count / 2))
        data_vertices_per_line = np.repeat(int(self.feature_count / 2), self.sample_count)

        return xy_coord, color_array, data_plot_indices, data_vertices_per_line

    def getAxesVertices(self):
        axes_count = 2
        axes_vertices = [[-0.8, -0.8], [-0.8, 0.8], [-0.8, -0.8], [0.8, -0.8]]
        axes_color = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        axes_index_starts = [0, 2]
        axes_vertex_count = [2, 2]

        return axes_vertices, axes_color, axes_index_starts, axes_vertex_count, axes_count

    def getMarkerVertices(self):
        return None

    def getLabelInformation(self):
        return None