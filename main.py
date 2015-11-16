import argparse
import PictureMover

parser = argparse.ArgumentParser(description='Move files from a work directory to a destination directory ' \
											 'and sort them into folders based on their creation date.')
parser.add_argument('workdirectory', help='the directory that contins the files that should be moved')
parser.add_argument('destinationdirectory', help='the directory that the files should be moved to')
parser.add_argument('extensions', nargs='+', help='what files should be moved eg. jpg mp4 etc.')

args = parser.parse_args()

pictureMover = PictureMover.PictureMover(args.workdirectory, args.destinationdirectory, args.extensions);

pictureMover.do_work()