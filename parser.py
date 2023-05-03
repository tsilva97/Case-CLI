# importing required modules
import argparse

# create a parser object
parser = argparse.ArgumentParser(description = "A simple CLI to consume Kafka messages")

# add argument
parser.add_argument("msgPartition", nargs = 1, metavar = "messagePartition", type = int,
					help = "Enter the desired partition for the topic message")

# add argument
parser.add_argument("locationPartition", nargs = 1, metavar = "locationPartition", type = int,
					help = "Enter the desired artition for the topic device-location")


def readArgs():
    # create a parser object
    print("hey")
    parser = argparse.ArgumentParser(description = "A simple CLI to consume Kafka messages")

    # add argument
    parser.add_argument("msgPartition", nargs = 1, metavar = "messagePartition", type = int,
                        help = "Enter the desired partition for the topic message")

    # add argument
    parser.add_argument("locationPartition", nargs = 1, metavar = "locationPartition", type = int,
                        help = "Enter the desired artition for the topic device-location")

    args = parser.parse_args()

    return args.msgPartition[0], args.locationPartition[0]

