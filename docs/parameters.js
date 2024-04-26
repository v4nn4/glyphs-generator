let load_parameters = () => {
  return {
    parent_strokes: [
      { x0: -1.0, y0: -1.0, x1: -1.0, y1: 1.0 },
      { x0: -1.0, y0: -1.0, x1: 1.0, y1: -1.0 },
      { x0: -1.0, y0: -1.0, x1: 1.0, y1: 1.0 },
      { x0: -1.0, y0: -1.0, x1: 0.0, y1: 0.0 },
      { x0: -1.0, y0: -1.0, x1: -1.0, y1: 0.0 },
      { x0: -1.0, y0: -1.0, x1: 1.0, y1: 0.0 },
      { x0: -1.0, y0: -1.0, x1: 0.0, y1: 1.0 },
      { x0: -1.0, y0: -1.0, x1: 0.0, y1: -1.0 },
      { x0: -1.0, y0: 1.0, x1: 1.0, y1: -1.0 },
      { x0: -1.0, y0: 1.0, x1: 1.0, y1: 1.0 },
      { x0: -1.0, y0: 1.0, x1: 0.0, y1: 0.0 },
      { x0: -1.0, y0: 1.0, x1: -1.0, y1: 0.0 },
      { x0: -1.0, y0: 1.0, x1: 1.0, y1: 0.0 },
      { x0: -1.0, y0: 1.0, x1: 0.0, y1: 1.0 },
      { x0: -1.0, y0: 1.0, x1: 0.0, y1: -1.0 },
      { x0: 1.0, y0: -1.0, x1: 1.0, y1: 1.0 },
      { x0: 1.0, y0: -1.0, x1: 0.0, y1: 0.0 },
      { x0: 1.0, y0: -1.0, x1: -1.0, y1: 0.0 },
      { x0: 1.0, y0: -1.0, x1: 1.0, y1: 0.0 },
      { x0: 1.0, y0: -1.0, x1: 0.0, y1: 1.0 },
      { x0: 1.0, y0: -1.0, x1: 0.0, y1: -1.0 },
      { x0: 1.0, y0: 1.0, x1: 0.0, y1: 0.0 },
      { x0: 1.0, y0: 1.0, x1: -1.0, y1: 0.0 },
      { x0: 1.0, y0: 1.0, x1: 1.0, y1: 0.0 },
      { x0: 1.0, y0: 1.0, x1: 0.0, y1: 1.0 },
      { x0: 1.0, y0: 1.0, x1: 0.0, y1: -1.0 },
      { x0: 0.0, y0: 0.0, x1: -1.0, y1: 0.0 },
      { x0: 0.0, y0: 0.0, x1: 1.0, y1: 0.0 },
      { x0: 0.0, y0: 0.0, x1: 0.0, y1: 1.0 },
      { x0: 0.0, y0: 0.0, x1: 0.0, y1: -1.0 },
      { x0: -1.0, y0: 0.0, x1: 1.0, y1: 0.0 },
      { x0: -1.0, y0: 0.0, x1: 0.0, y1: 1.0 },
      { x0: -1.0, y0: 0.0, x1: 0.0, y1: -1.0 },
      { x0: 1.0, y0: 0.0, x1: 0.0, y1: 1.0 },
      { x0: 1.0, y0: 0.0, x1: 0.0, y1: -1.0 },
      { x0: 0.0, y0: 1.0, x1: 0.0, y1: -1.0 },
    ],
    intersection_matrix: [
      [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0,
        0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0,
      ],
      [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
        0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1,
      ],
      [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1,
      ],
      [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0,
        0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1,
      ],
      [
        1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,
        0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0,
      ],
      [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1,
        0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1,
      ],
      [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1,
      ],
      [
        1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0,
        0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1,
      ],
      [
        1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1,
      ],
      [
        1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1,
        1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1,
      ],
      [
        1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0,
        0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1,
      ],
      [
        1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0,
        0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0,
      ],
      [
        1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1,
        0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1,
      ],
      [
        1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1,
      ],
      [
        1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0,
        0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1,
      ],
      [
        0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0,
      ],
      [
        0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1,
      ],
      [
        1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,
        0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1,
      ],
      [
        0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1,
        0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0,
      ],
      [
        0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0,
        1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1,
      ],
      [
        0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
        0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1,
      ],
      [
        0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1,
      ],
      [
        1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1,
        1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1,
      ],
      [
        0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1,
        1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0,
      ],
      [
        0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1,
        1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1,
      ],
      [
        0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1,
        1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1,
      ],
      [
        1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0,
        0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1,
      ],
      [
        0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1,
        0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1,
      ],
      [
        0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0,
        1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1,
      ],
      [
        0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1,
      ],
      [
        1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
      ],
      [
        1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0,
        1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1,
      ],
      [
        1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0,
        0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1,
      ],
      [
        0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1,
        1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1,
      ],
      [
        0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1,
        0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1,
      ],
      [
        0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
      ],
    ],
    transformation_matrix: [
      [0, 15, 9, 1, 9, 15, 1],
      [9, 1, 0, 0, 15, 9, 15],
      [8, 8, 8, 2, 2, 2, 8],
      [10, 16, 10, 3, 21, 21, 16],
      [11, 18, 13, 7, 24, 23, 20],
      [12, 17, 14, 6, 25, 22, 19],
      [14, 19, 12, 5, 22, 25, 17],
      [13, 20, 11, 4, 23, 24, 18],
      [2, 2, 2, 8, 8, 8, 2],
      [1, 9, 15, 15, 0, 1, 0],
      [3, 21, 21, 16, 10, 16, 3],
      [4, 23, 24, 20, 13, 18, 7],
      [5, 22, 25, 19, 14, 17, 6],
      [7, 24, 23, 18, 11, 20, 4],
      [6, 25, 22, 17, 12, 19, 5],
      [15, 0, 1, 9, 1, 0, 9],
      [21, 3, 3, 10, 16, 10, 21],
      [22, 5, 6, 14, 19, 12, 25],
      [23, 4, 7, 13, 20, 11, 24],
      [25, 6, 5, 12, 17, 14, 22],
      [24, 7, 4, 11, 18, 13, 23],
      [16, 10, 16, 21, 3, 3, 10],
      [17, 12, 19, 25, 6, 5, 14],
      [18, 11, 20, 24, 7, 4, 13],
      [20, 13, 18, 23, 4, 7, 11],
      [19, 14, 17, 22, 5, 6, 12],
      [26, 27, 28, 29, 28, 27, 29],
      [27, 26, 29, 28, 29, 26, 28],
      [29, 28, 27, 27, 26, 29, 26],
      [28, 29, 26, 26, 27, 28, 27],
      [30, 30, 35, 35, 35, 30, 35],
      [32, 33, 33, 34, 31, 34, 32],
      [31, 34, 31, 32, 33, 33, 34],
      [34, 31, 34, 33, 32, 32, 31],
      [33, 32, 32, 31, 34, 31, 33],
      [35, 35, 30, 30, 30, 35, 30],
    ],
  };
};

export default { load_parameters };
