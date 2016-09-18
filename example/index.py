import rinobot_plugin as bot
import numpy as np

def main():
    # lets get our parameters and data
    filepath = bot.filepath()
    data = bot.loadfile(filepath)

    # now comes the custom plugin logic
    algo = bot.get_arg('algo', type=str, required=True)
    index = bot.index_from_args(data)

    if algo == "sum":
        data[index] = np.array([col/col.sum() for col in data[index].T]).T
    elif algo == "max":
        data[index] = np.array([col/col.max() for col in data[index].T]).T

    outname = bot.no_extension() + '-normalize-%s.txt' % algo

    # then we set up the output
    outpath = bot.output_filepath(outname)
    np.savetxt(outpath, data)

if __name__ == "__main__":
    main()
