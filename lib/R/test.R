library(ggplot2)

df <- mtcars
#Data and aesthetics
pl <- ggplot(data = df, aes(x = wt, y = mpg))
#Geometry
#print(pl + geom_point(alpha = 0.5, size = 5))
#print(pl + geom_point(aes(size = hp)))
#print(pl + geom_point(aes(size = factor(cyl))))
print(pl + geom_point(aes(shape = factor(cyl), color = factor(cyl)), size = 3)) # color can be a character or hex value
pl2 <- pl + geom_point(aes(color = hp), size = 3)
pl3 <- print(pl2 + scale_color_gradient(low = "blue", high = "red"))
print(pl3)
