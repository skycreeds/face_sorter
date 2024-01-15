
# pic_sorter

A cli tool to seperate images containing provided face 




## Installation

#pip installation

```python
   pip3 install git+https://github.com/skycreeds/pic_sorter.git
```

## Usage/Examples

#Usage
```bash
flags :
    --face_pic:provide path of image with a single face_pic

    --folder_in: provide path of folder to work on (contain images in jpg or png) default is current directory

    --folder_out: provide path to folder to hold out put.Default is current directory

    --tolerence: accuracy of recognition(smaller is better but intensive) range(0,1) 0.5 is best 

    --encode_resample:times to resample face encodings(lager is better but intensive) integer 
    
    --location_resample:times to resample face locations(larger better but intensive) integer
```

#Example
```bash
    pic_sorter --face_pic face.jpeg --folder_in '/sample' --folder_out 'out/' --tolerence 0.3 --encode_resample 2 --location_resample 2

```




## Alert


Use tolerence,encode_resample,location_resample while keeping ram in mind.Lower tolerence,higher resampling uses more ram and can crash.

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Authors

- [@skycreeds](https://www.github.com/skycreeds)

