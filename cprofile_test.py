import cProfile
import palingrams
import load_dict
word_list = load_dict.load('2of4brif.txt')
cProfile.run('palingrams.find_palingrams(word_list)')
