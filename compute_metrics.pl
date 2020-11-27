#! /usr/bin/perl -w

use strict;

if ($#ARGV < 2){
	die();
}
my ($truth, $result, $num_nuc) = @ARGV;

my $num_region = `wc -l $truth |cut -d \" \" -f 1`;
chomp($num_region);

sub find_sum {
	my ($input) = @_;
	my @line_list = split("\n", $input);
	my $sum = 0;
	foreach my $line (@line_list){
		# print "Line is $line\n";
		my @split_line = split("\t", $line);
		# print("@split_line\n");
		$sum = $sum + $split_line[2] - $split_line[1];
	}
	# $sum =~ s/^\s+|\s+$//g;
	return $sum;
}


# print("$truth $result\n");

# Number of true nucleotides
my $T = `bedtools intersect -a $truth -b $truth  -wo | cut -f 7 | paste -sd+ | bc `;
chomp($T);

my $TP = `bedtools intersect -a $truth -b $result  -wo | cut -f 7 | paste -sd+ | bc `;
chomp($TP);

my $FP = `bedtools subtract -a $result -b $truth`;
$FP = find_sum($FP);

my $FN = `bedtools subtract -a $truth -b $result`;
$FN = find_sum($FN);

my $TN = $num_region * 
$num_nuc 
- ($FN + $TP + $FP);


my $accuracy = ($TP + $TN) / ($TP + $TN + $FP + $FN);
my $precision = $TP / ($TP + $FP);
my $recall = $TP / ($TP + $FN);
my $FMeasure = 2 * $precision * $recall / ($precision + $recall);
my $FPR = $FP / ($FP + $TN);
print("TP\tFP\tFN\tTN\tAccuracy\tFPR\tPrecision\tRecall\tF-measure\n");
print("$TP\t$FP\t$FN\t$TN\t$accuracy\t$FPR\t$precision\t$recall\t$FMeasure\n");








