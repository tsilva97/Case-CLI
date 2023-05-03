# DeepDive Case CLI

This project does the following: 
- Expects two arguments (int) and automaticlaly connects to a kafka server running on localhost 
and consumes messages from the topics "messages" and "device-location" on the indicated partitions

## Example Usage

```command
python main.py 0 3
```
Consumes messages from partition 0 of "messages" and partition 3 of "device-location" 

## Dependencies

Before using this program please install kafka-python by running
```command
pip install kafka-python
```
This program also depends on the docker-compose.yml found in the DeepDive Case API that sets up the kafka server and on the server being correctly configured.


## Possible Improvements

- Pass the topic names and kafka host as env vars
- Add better logging (maybe time at which the message are captured)
- Add tests
- Better input validation (number in range 0 to 3 or for more flexibility just check if the number is not negative)


