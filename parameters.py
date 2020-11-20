
run_parameters = {
    'return_layer': 'fc6',
    'model': 'vggface',
    'vgg_finetune': 'conv5_1,conv5_2,conv5_3,fc6',
    'train_batch_size': 100,
    'test_batch_size': 160,
    'dimension': 4096,
    'epoch': 6,
    'print_epoch': 1,
    'lambda1': 3.0,
    'lambda2': 1.0,
    'lambda3': 1.0,
    'lambda4': 1.0,
    'alpha': 0.8,
    'std_dev': 1.0,
    'multi_gpu': 1,
    'apply_inm': 0,
    'white_noise': 1,
    'use_pc': 1
}

dataset_parameters = {
    'replayattack': {
        'path': '/home/yashasvi/external/Datasets/replayattack/bk_new_extracted_faces',
        'train': {
        'id_list': [1, 2, 4, 6, 7, 8, 12, 16, 18, 25, 27, 103, 105, 108, 110],
        'id_dic': {1:0, 2:1, 4:2, 6:3, 7:4, 8:5, 12:6, 16:7, 18:8, 25:9, 27:10, 103:11, 105:12, 108:13, 110:14}
        },

        'devel': {
        'id_list': [3, 5, 10, 15, 17, 22, 29, 30, 101, 111, 113, 114, 116, 118, 119],
        'id_dic': {3:0, 5:1, 10:2, 15:3, 17:4, 22:5, 29:6, 30:7, 101:8, 111:9, 113:10, 114:11, 116:12, 118:13, 119:14}
        },

        'test': {
        'id_list': [9, 11, 13, 14, 19, 20, 21, 23, 24, 26, 28, 31, 102, 104, 106, 107, 109, 112, 115, 117],
        'id_dic': {9:0, 11:1, 13:2, 14:3, 19:4, 20:5, 21:6, 23:7, 24:8, 26:9, 28:10, 31:11, 102:12, 104:13, 106:14, 107:15, 109:16, 112:17, 115:18, 117:19}
        }
    },
    'replaymobile': {
        'path': '/home/yashasvi/external/Datasets/replaymobile/faces',
        'train': {
        'id_list': [1, 3, 8, 11, 12, 16, 18, 20, 26, 34, 37, 38],
        'id_dic': {1:0, 3:1, 8:2, 11:3, 12:4, 16:5, 18:6, 20:7, 26:8, 34:9, 37:10, 38:11}
        },
        'devel': {
        'id_list': [5, 6, 13, 14, 15, 23, 24, 25, 28, 29, 31, 32, 35, 36, 39, 40],
        'id_dic': {5:0, 6:1, 13:2, 14:3, 15:4, 23:5, 24:6, 25:7, 28:8, 29:9, 31:10, 32:11, 35:12, 36:13, 39:14, 40:15}
        },
        'test': {
        'id_list': [2, 4, 7, 10, 17, 19, 21, 22, 27, 30, 33],
        'id_dic': {2:0, 4:1, 7:2, 10:3, 17:4, 19:5, 21:6, 22:7, 27:8, 30:9, 33:10}
        }
    },
    'rose_youtu': {
        'path': '/home/yashasvi/external/Datasets/rose_youtu/faces',
        'train': {
        'id_list': [2, 3, 4, 5, 6, 7, 9, 10, 11, 12],
        'id_dic': {2:0, 3:1, 4:2, 5:3, 6:4, 7:5, 9:6, 10:7, 11:8, 12:9}
        },
        'devel': {
        'id_list': [2, 3, 4, 5, 6, 7, 9, 10, 11, 12],
        'id_dic': {2:0, 3:1, 4:2, 5:3, 6:4, 7:5, 9:6, 10:7, 11:8, 12:9}
        },
        'test': {
        'id_list': [13, 14, 15, 16, 17, 18, 20, 21, 22, 23],
        'id_dic': {13:0, 14:1, 15:2, 16:3, 17:4, 18:5, 20:6, 21:7, 22:8, 23:9}
        }
    },
    'oulu_npu': {
        'path': '/home/yashasvi/external/Datasets/Oulu_NPU/',
        'train': {
        'id_list': range(1, 21),
        'id_dic': {1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8, 10:9, 11:10, 12:11, 13:12, 14:13, 15:14, 16:15, 17:16, 18:17, 19:18, 20:19}
        },
        'devel': {
        'id_list': range(21, 36),
        'id_dic': {21:0, 22:1, 23:2, 24:3, 25:4, 26:5, 27:6, 28:7, 29:8, 30:9, 31:10, 32:11, 33:12, 34:13, 35:14}
        },
        'test': {
        'id_list': range(36, 56),
        'id_dic': {36:0, 37:1, 38:2, 39:3, 40:4, 41:5, 42:6, 43:7, 44:8, 45:9, 46:10, 47:11, 48:12, 49:13, 50:14, 51:15, 52:16, 53:17, 54:18, 55:19}
        }
    },
    'spoof_in_wild': {
        'path': '/home/yashasvi/external/Datasets/spoof_in_wild/SiW_database/SiW_release/extracted_faces/',
        'train': {
        'id_list': [],
        'id_dic': {}
        },
        'devel': {
        'id_list': [],
        'id_dic': {}
        },
        'test': {
        'id_list': [],
        'id_dic': {}
        }
    },
    'msu_mfsd': {
        'path': '/home/yashasvi/external/Datasets/MSU-MFSD/scene01/img/',
        'train': {
        'id_list': [2, 3, 5, 6, 7, 8, 9, 11, 12, 21, 22, 34, 53, 54, 55],
        'id_dic': {2:0, 3:1, 5:2, 6:3, 7:4, 8:5, 9:6, 11:7, 12:8, 21:9, 22:10, 34:11, 53:12, 54:13, 55:14}
        },
        'devel': {
        'id_list': [2, 3, 5, 6, 7, 8, 9, 11, 12, 21, 22, 34, 53, 54, 55],
        'id_dic': {2:0, 3:1, 5:2, 6:3, 7:4, 8:5, 9:6, 11:7, 12:8, 21:9, 22:10, 34:11, 53:12, 54:13, 55:14}
        },
        'test': {
        'id_list': [1, 13, 14, 23, 24, 26, 28, 29, 30, 32, 33, 35, 36, 37, 39, 42, 48, 49, 50, 51],
        'id_dic': {1:0, 13:1, 14:2, 23:3, 24:4, 26:5, 28:6, 29:7, 30:8, 32:9, 33:10, 35:11, 36:12, 37:13, 39:14, 42:15, 48:16, 49:17, 50:18, 51:19}
        }
    }


}