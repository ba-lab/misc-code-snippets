# Native R
Some references:
* http://research.stowers-institute.org/efg/R/Color/Chart/ColorChart.pdf
* http://rgraphics.limnology.wisc.edu/images/miscellaneous/pch.png
* http://research.stowers-institute.org/mcm/plotlayout.pdf

### A sample code
```R
setwd("~/Dropbox/manuscripts/conassess")
data <- read.table(“abc.txt”, skip = 1, header = T)
data$V7 <- abs(data$V1-data$V2)

for(i in 1:10) {
	print(usq[i])
}

all = read.table("jobs/14/feats/win-7_train.feat.txt", header = F)
cor(  all$V1, all$V598, method="pearson")
summary(all)
fileconn = file("results.txt")
writeLines(summary(all), fileconn)
close(fileconn)
```

### Computing correlation in R for two vectors a and b:
```R
coeff <- cor(a, b, method="spearman")
coeff <- cor(a, b, method="pearson")
```
### Replacing data values
```R
data$V7[data$V7 > 23] <- 200
```
### Subsetting data
```R
selection1 <- subset(alldata, EVAL == "TMSCORE")
chr1 <- data[which(data$V1 == 1),]
alldata <- subset(alldataoriginal, alldataoriginal$RMSD < 20.0)
```
### Combine data into a new table
```R
stage1 <- data.frame(tmscore = alldata$stage1_TM.score, stage = rep(c("stage1"), each = 150))
stage2 <- data.frame(tmscore = alldata$stage2_TM.score, stage = rep(c("stage2"), each = 150))
final  <- rbind(stage1, stage2)
```
### Set number of plots in one image, and adjust figure margins
```
par(mar=c(2,2,1,0.1))
```

### XY plot with selected columns
plot(data[, 'Dist'], data[, 'ENOE'])
lines(data[,'ENOE'],col='red',lty=3)

### Plot to file
```R
png(filename="C:/temp/name.png", height = 1600, width = 1600, res=300)
dev.off()
```

### XY plot with grouped data
```R
axis(1, at=1:5, labels=c("a","b","c","d","e"))
lines(trucks,col='red',lty=3) 
cars<-c(1,3,6,4,9) 
trucks <- c(2, 5, 4, 5, 12)
g_range <- range(0, cars, trucks) 
plot(cars, col="blue", type='l', ylim=g_range, xaxt='n')
axis(1, at=1:5, labels=c("a","b","c","d","e"))
lines(trucks,col='red',lty=3) 
```

### Quick box plot
```R
data <- read.table("/tmp/abc.txt", header=F)
hist(data$V1)
axis(1, seq(0, 600, by=100))
```

### Filled Density Plot
```R
d <- density(mtcars$mpg)
plot(d, main="Kernel Density of Miles Per Gallon")
polygon(d, col="red", border="blue")
```

### Tip: 
The actual values of variables are used only when the plots are actually printed. So, separate variables must be used for separate plots within same image!

# ggplot2

### A sample code
```R
require("ggplot2")
require("gridExtra")
alldata <- read.table(file="correlation.txt", header=T) 
png(filename = "correlation.png", width = 1000, height = 600, res=100)
plot1 <- ggplot(...) + …
plot2 <- ggplot(...) + ...
grid.arrange(plot1, plot2, ncol = 2)
dev.off()
```

### XY plot with grouped data
```R
ggplot(data = selection1, aes(selection1$ID, selection1$Correlation)) +
geom_point(aes(colour = factor(selection1$Measure))) +
geom_line(aes(colour = factor(selection1$Measure))) +
xlab("Selected Top Contacts") +
ylab("|Pearson correlation| with TM-score") +
```
### Replace the X-axis tick labels
```R
scale_x_discrete(labels = unique(selection1$TopxL)) + 
theme_bw() +
theme(legend.position = "top", legend.title=element_blank())
```

### Density plot
```R
pl1 <- ggplot(data, aes(x = data$TM_score, fill = data$method, linetype = data$method, colour = data$method)) +
geom_density(alpha = 0.2) +
xlab("TM-score") + ylab("Density of best models") +
scale_colour_discrete( breaks=c("sheet", "cns_only", "modeller", "tinker"), labels=c("CONFOLD", "CNS", "Modeller", "Reconstruct")) +
scale_linetype_discrete( breaks=c("sheet", "cns_only", "modeller", "tinker"), labels=c("CONFOLD", "CNS", "Modeller", "Reconstruct")) +
scale_fill_discrete( breaks=c("sheet", "cns_only", "modeller", "tinker"), labels=c("CONFOLD", "CNS", "Modeller", "Reconstruct")) +
theme_bw() +
theme(legend.position = "top", legend.title=element_blank())
print(pl1)
```

### Bar diagrams
```
ggplot(alldata, aes(x = alldata$xL, y = alldata$contact_count, fill = alldata$stage)) +
	geom_bar(stat="identity", position=position_dodge(), colour = "black") +
	xlab("number of contacts (top-xL)") + ylab("number of best models (out of 150)") +
	theme_bw() +
	scale_x_continuous(breaks=c(0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2)) +
	theme(legend.position = "top", legend.title=element_blank())
```

### Box Plot
```R
pl1 <-	ggplot(feature.scores, aes(y = feature.scores$PrecisionL5, x = feature.scores$FeatureLabel, fill = feature.scores$FeatureLabel)) +
  geom_boxplot(aes(group = cut_width(feature.scores$FeatureLabel, 1)), alpha = 0.2, color = "darkgreen", outlier.size = 0) +
  xlab("Separation between two points") + ylab("Distance") +
  theme_bw() +
  theme(legend.position = "none", legend.title=element_blank()) +
  labs(title = "Chromosome3D")
```
