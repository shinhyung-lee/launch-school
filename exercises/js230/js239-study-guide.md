
# JS230 Topics


Q. When is the DOM different than the HTML?
- when there are mistakes in the HTML and the browser has fixed them for you.
- Let’s say you have a `<table>` element in your HTML and leave out the required `<tbody>` element. The browser will just insert that `<tbody>` for you.
- It will be there in the DOM, so you’ll be able to find it with JavaScript and style it with CSS, even though it’s not in your HTML. (!!!!!)

## Javascript vs. the DOM
- JavaScript is a language that the browser reads and does stuff with.
- But the DOM is where that stuff happens. 
- In fact a lot of what you might think of as a “JavaScript Thing” is more accurately a “DOM API”.
- The DOM is the lifeblood here. It’s where everything goes down in the browser. 
    - JavaScript is just the syntax, the language. 
    - It (Javascript) can be used totally outside the browser with no DOM APIs at all (see Node.js)

What is a node?
- in the context of DOM, a node is a single point in the node tree, such as the document itself, HTML elements, text, and comments.

JS Methods to interact with DOM
- `querySelector`: returns the first node in the DOM that matches the specified CSS selector
- `querySelectorAll`: 
- `document` node
    - represents the entire HTML document
    - is the topmost node
- `toString` method
```javascript
document.toString()
// "[object HTMLDocument]"
```

Node Properties
- `nodeName`
    - contains a String that represents the node type
    - For Elements (anything that represents an HTML tag), this is the name of the corresponding tag in <b><span style='color: red;'>uppercase</span><b>
```javascript
> p.nodeName
= "P"
```

- For text nodes -- even empty nodes -- the nodeName is "#text". For comments, it's "#comment".

`nodeType` property
- to determine a node's type
- returns a number that matches a node type constant 

```javascript
> p.nodeType
= 1
```

Most common Node Types (make a table)
```table
Constant	       Value	Description
Node.ELEMENT_NODE	1	An Element representing an HTML tag
Node.TEXT_NODE	    3	A Text node
Node.COMMENT_NODE	8	A Comment node
Node.DOCUMENT_NODE	9	A Document node
```

`nodeValue` property
- references the value of a node
- Element nodes don't have values:
```javascript
> p.nodeValue
= null
```

- Text nodes have `nodeValue`
- For a text node, the nodeValue is the textual content of the node
```javascript
> let t = p.childNodes[0];
> t.nodeName;
= "#text"
> t.toString();
= "[object Text]"
> t.nodeValue
= "\n      To receive our weekly emails, enter your email address below.\n"
```

## Attribute Properties
- We can access some attributes directly
- The DOM exposes these special attributes as properties of the Element: `id`, `name`, `title`, and `value`
    - We can FETCH the value for one of these properties or SET it to a new value using standard property access and assignment operations
- class attribute is similar but uses the `className` property since class is a JavaScript reserved word
```javascript
> p.className;
= "intro"
> p.className = 'outro';
```

`classList` attribute
- Working with the class attribute via `className` is inconvenient when elements have more than one class
```html
<button class="btn btn-lg btn-primary">Proceed</button>
```

Getting the list of classes for the `button`
```javascript
> button.className;
= "btn btn-lg btn-primary"
```

## `classList` and array-like DOMTokenList object
- array-like DOMTokenList object has these properties and methods

| Name	| Description |
| -------- | -------- |
| add(name)| 	Add class name to element| 
| remove(name)	| Remove class name from element| 
| toggle(name)	| Add class name to element if it doesn't exist, remove if it does exist| 
| contains(name)	| Return true or false depending on whether element has class name| 
| length	| The number of classes to which element belongs| 

## `style` and CSSStyleDeclaration object
- Element nodes also have a style attribute that has some special behavior. 
- The `style` attribute on an Element references a CSSStyleDeclaration Object
- We can use the style attribute to alter any CSS property
- To remove a CSS property, set the property to null with the style property:
```javascript
> h1.style.color = null;
```

(IMPORTANT)
- When a CSS property's name contains dashes, you must use a camelCased version of the name to access that property.
    - For example, to set a value for the line-height attribute, you assign a value to the lineHeight property:
```javascript
> h1.style.lineHeight = '3em';
```
(BUT WHY?)
- because dashes (hyphens) are interpreted as the subtraction operator in JavaScript syntax\
(ie)
```javascript
element.style.background-color = "red"; 
```
The JavaScript engine evaluates that statement as:
1. Get the value of element.style.background
2. Subtract (-) the value of the variable color
3. Try to assign "red" to the resulting mathematical expression

=> Because evaluating an expression on the left-side of an equals sign is illegal syntax, the engine throws a ReferenceError or SyntaxError
```javascript
NaN - color
// Uncaught ReferenceError: color is not defined
```

| Parent Node Method	| Description |
| -------- | -------- |
| parent.appendChild(node)| 	Append node to the end of parent.childNodes | 
| parent.insertBefore(node, targetNode)| 	Insert node into parent.childNodes before targetNode | 
| parent.replaceChild(node, targetNode)| 	Remove targetNode from parent.childNodes and insert node in its place | 

- `document.appendChild` causes an error. Use `document.body.appendChild` instead.

(IMPORTANT)
- No Node may appear twice in the DOM. If you try to add a node that is already in the DOM, it gets removed from the original location. Thus, you can move an existing node by inserting it where you want it.

These methods insert a node before, after, or within an Element:
| Element Insertion Method | Description |
| ------ | ----- |
| element.insertAdjacentElement(position, newElement) | Inserts newElement at position relative to element |
| element.insertAdjacentText(position, text) | Inserts Text node that contains text at position relative to element |  

`position` must be one of the following String values:
| Position | Description | 
| ------ | ------ | 
| "beforebegin" | Before the element | 
| "afterbegin" | Before the first child of the element | 
| "beforeend" | After the last child of the element | 
| "afterend" | After the element | 











