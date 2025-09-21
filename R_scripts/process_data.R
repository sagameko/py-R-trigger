args <- commandArgs(trailingOnly = TRUE)
if (length(args) < 2) {
  stop("Usage: Rscript r_scripts/process_data.R <in_csv> <out_csv>")
}

in_csv  <- args[[1]]
out_csv <- args[[2]]

cat("[R] Reading:", in_csv, "\n")
dat <- read.csv(in_csv, stringsAsFactors = FALSE)

if (!all(c("x","y") %in% names(dat))) {
  stop("Input CSV must have columns 'x' and 'y'")
}

dat$z <- dat$x + dat$y

cat("[R] Writing:", out_csv, "\n")
dir.create(dirname(out_csv), showWarnings = FALSE, recursive = TRUE)
write.csv(dat, out_csv, row.names = FALSE)

cat("[R] Done. Rows:", nrow(dat), "\n")
