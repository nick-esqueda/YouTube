// import React, { useContext, useRef, useState } from 'react'
// import { createContext } from 'react'

// const PathnameContext = createContext();
// export const usePathname = () => useContext(PathnameContext);

// export default function PathnameProvider(props) {
//   const [isVideoPage, setIsVideoPage] = useState(window.location.pathname.startsWith('/watch'));
  
//   return (
//     <PathnameContext.Provider value={{ isVideoPage, setIsVideoPage }}>
//       {props.children}
//     </PathnameContext.Provider>
//   )
// }
