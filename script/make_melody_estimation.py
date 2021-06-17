from pathlib import Path
import argparse
import _pickle as pickle
#from test_qbh import QbhSystem
from utils.data_utils import get_song_ids_of_selected_genre
from utils.melody_utils import MelodyLoader

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_dir', type=Path,
                        default= Path('/home/svcapp/t2meta/flo_new_music/music_100k/'),
                        help='directory to load checkpoint')
    parser.add_argument('--meta_dat_path', type=str,
                        default= 'data/flo_metadata_220k.dat',
                        help='directory to load metadata')
    parser.add_argument('--humm_db_ids_path', type=str,
                default= 'data/humm_db_ids.dat',
                help='directory to load humm_db_ids')
    parser.add_argument('--device', type=str, default='cuda',
                             help='cpu or cuda')

    args = parser.parse_args()

    with open(args.meta_dat_path, 'rb') as f:
        db_metadata = pickle.load(f)
    selected_genres = [4, 12, 13, 17, 10, 7,15, 11, 9]
    song_ids = get_song_ids_of_selected_genre(db_metadata, selected_genres)

    with open(args.humm_db_ids_path, 'rb') as f:
        humm_ids = pickle.load(f)
    song_ids += humm_ids

    melody_loader = MelodyLoader(args.dataset_dir)
    melody_loader.check_txt_exists(song_ids, make_txt=True, verbose=True)
