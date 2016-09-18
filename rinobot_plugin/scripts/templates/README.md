# rinobot-plugin

Makes an line plot of xy or xyyy data.

So if your data has many columns, this package will take the
first column as the x axis, and each subsequent column as
different y plots.

If you have a `data.txt` file with the following content

```
0.0 8.7
1.4 2.4
2.4 2.3
3.3 3.5
4.1 7.3
...
...
```

This plugin will make a png called `data-line-plot.png`:

<img src="examples/xyyy-line-plot.png" width="600">


## Arguments:

In the extra args section of the rinobot automation config you can set the following parameters

Extra args:
```
--xmin=2 --xmax=5 --ymin=1 --ymax=90
```

You can set all or none of these parameters.
