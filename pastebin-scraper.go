package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	/*
		type J struct {
			Hello string `json:"hello"`
		}
	*/
	URL := "http://pi/json/j.json"
	resp, err := http.Get(URL)
	if err != nil {
		fmt.Println(err)
	}

	defer resp.Body.Close()

	jsonBody, jsonErr := ioutil.ReadAll(resp.Body)
	if jsonErr != nil {
		fmt.Println(jsonErr)
	}

	var data map[string]interface{}

	unmarshalErr := json.Unmarshal([]byte(jsonBody), &data)
	if unmarshalErr != nil {
		fmt.Println(unmarshalErr)
	}

	fmt.Println(data["hello"])
	//fmt.Println(err)

}
