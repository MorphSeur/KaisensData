# Kaisens Data
## [app.py](https://github.com/MorphSeur/KaisensData/blob/master/app.py)

To run an example:
- Start the analytic server:
    ```sh
    $ python app.py
    ```

## Requirements
- Please refer to [requirements.txt](https://github.com/MorphSeur/KaisensData/blob/master/requirements.txt).
- Python 3.7.7 was used.

## Dockerfile
Dockerfile contains necessary libraries to face recognition analytic.
- To build the docker
    ```
    $ sudo docker build --tag face_recognition .
    ```
- Or
    ```
    $ docker-compose up
    ```
- In browser
    ```
	$ ipAddressOfVM:14484/extract
    ```