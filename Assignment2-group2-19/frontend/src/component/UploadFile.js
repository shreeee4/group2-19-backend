// Shreeya Shrestha - 103831863
import React, { useState } from "react";
import Button from "@mui/material/Button";
import axios from 'axios';

function Upload() {
  //storing the selected file 
  const [FileSelected, SetFileSelected] = useState(null);

  //handle the file selection event
  const FileSelectEvent = (event) => {
    const file = event.target.files[0];
    SetFileSelected(file);
  };

  //handle the file uploading event
  const FileUploadEvent = async () => {
    if (FileSelected) {
        // Create a FormData object to send the file
        const formData = new FormData();
        formData.append("file", FileSelected);
        try {
          // Make a POST request to your API endpoint
          await axios.post("http://localhost:8000/audit/", formData, {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          });

          alert("File " + FileSelected.name + " uploaded and audited.");
      } catch (error) {
        alert("Error uploading and auditing file: " + error);
      }
    } else {
      alert("Invalid File Selection.");
    }
  };

  return (
    <div>
      {/* input file type  */}
      <input
        type="file"
        accept=".sol"
        onChange={FileSelectEvent}
        style={{ display: "none" }}
        id="InputFile"
      />
      <label htmlFor="InputFile">
        {/* button to select file  */}
        <Button variant="contained" component="span">
          Select Smart Contract File (.sol)
        </Button>
      </label>
      {/* button to upload file  */}
      <Button
        variant="contained"
        color="primary"
        onClick={FileUploadEvent}
        //disable button while file is not selected to avoid blank submissions
        disabled={!FileSelected}
      >
        Upload
      </Button>
    </div>
  );
}

export default Upload;                                  
