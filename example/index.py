
import rinobot_plugin as bot
import numpy as np

def main():
  # lets get our parameters and data
  filepath = bot.filepath()
  data = bot.loadfile(filepath)

  # now comes the custom plugin logic
  shift = bot.get_arg('shift', type=float)
  index = bot.index_from_args(data)
  data[index] = data[index] + shift
  outname = bot.no_extension() + '-shift-%s.txt' % shift

  # then we set up the output
  outpath = bot.output_filepath(outname)
  np.savetxt(outpath, data, fmt="%d")


if __name__ == "__main__":
  main()
