import React,{Component} from "react";

class ListComponent extends Component {
    render() 
    {
        return(
        <div>
            <ul>{this.props.TextList.map(text =>
                <li key={text}>
                    {text}
                </li>
                )}
            </ul>
        </div>);
    }
}
export default ListComponent;