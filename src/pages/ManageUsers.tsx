import { useState, useRef, useEffect } from "react";
import { NavbarAdmin } from "../components/NavbarAdmin";
import {
  AiFillEdit,
  AiFillCloseCircle,
  AiOutlineUserAdd,
} from "react-icons/ai";
import search_logo from "../assets/images/search_logo.png";
import Modal from "react-modal";
import "../css/ManageUsers.css";

interface Student {
  firstName: string;
  middleName?: string;
  lastName: string;
  email: string;
  studentID?: string;
  yearLevel?: string;
  program?: string;
  profilePic?: string;
  role: string[];
}

const ManageUsers: React.FC = () => {
  const API_BASE_URL = "http://localhost:8000"; // Replace with your actual API base URL
  const [profilePic, setProfilePic] = useState<File | null>(null);
  const [profilePicPreview, setProfilePicPreview] = useState<string>("");
  const [editProfilePic, setEditProfilePic] = useState<File | null>(null);
  const [editProfilePicPreview, setEditProfilePicPreview] = useState<string>("");
  const fileInputRef = useRef<HTMLInputElement>(null);
  const editFileInputRef = useRef<HTMLInputElement>(null);

  const [searchTerm, setSearchTerm] = useState("");
  const [users, setUsers] = useState<Student[]>([]);
  const [editIndex, setEditIndex] = useState<number | null>(null);
  const [deleteIndex, setDeleteIndex] = useState<number | null>(null);
  const [addUserModalOpen, setAddUserModalOpen] = useState(false);
  const [validationErrors, setValidationErrors] = useState<Record<string, string>>({});
  const [showStudentFields, setShowStudentFields] = useState(false);
  const [studentID, setStudentID] = useState("");
  const [yearLevel, setYearLevel] = useState("1");
  const [program, setProgram] = useState("");
  const [customProgram, setCustomProgram] = useState("");
  const [showCustomProgramInput, setShowCustomProgramInput] = useState(false);
  const [editStudentID, setEditStudentID] = useState("");
  const [editYearLevel, setEditYearLevel] = useState("1");
  const [editProgram, setEditProgram] = useState("");
  const [editCustomProgram, setEditCustomProgram] = useState("");
  const [showEditCustomProgramInput, setShowEditCustomProgramInput] = useState(false);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const [editedUser, setEditedUser] = useState<Student>({
    firstName: "",
    middleName: "",
    lastName: "",
    email: "",
    role: [],
  });

  const [newUser, setNewUser] = useState({
    firstName: "",
    middleName: "",
    lastName: "",
    email: "",
    password: "",
    role: [] as string[],
  });

  // Fetch all students on component mount
  useEffect(() => {
    const fetchStudents = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/students/all`);
        if (!response.ok) {
          throw new Error('Failed to fetch students');
        }
        const data = await response.json();
        // Map the API data to our student format
        const formattedStudents = data.map((student: any) => ({
          ...student,
          role: ["Student"], // All from this endpoint are students
          studentID: student.id, // Assuming id from API is studentID
        }));
        setUsers(formattedStudents);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'An unknown error occurred');
      } finally {
        setIsLoading(false);
      }
    };

    fetchStudents();
  }, []);

  // Handle profile picture upload
  const handleProfilePicChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const file = e.target.files[0];
      setProfilePic(file);
      setProfilePicPreview(URL.createObjectURL(file));
    }
  };

  const handleEditProfilePicChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const file = e.target.files[0];
      setEditProfilePic(file);
      setEditProfilePicPreview(URL.createObjectURL(file));
    }
  };

  const availableRoles = ["Admin", "Student", "SSG Officer", "Event Organizer"];
  const yearLevels = ["1", "2", "3", "4", "5"];
  const defaultPrograms = [
    "BS Computer Engineering",
    "BS Civil Engineering",
    "BS Electronics Engineering",
    "BS Electrical Engineering",
    "Other (Please specify)",
  ];
  const [roleDropdownOpen, setRoleDropdownOpen] = useState(false);
  const [editRoleDropdownOpen, setEditRoleDropdownOpen] = useState(false);
  const [programDropdownOpen, setProgramDropdownOpen] = useState(false);
  const [editProgramDropdownOpen, setEditProgramDropdownOpen] = useState(false);

  Modal.setAppElement("#root");

  const getFullName = (user: Student) => {
    return [user.firstName + user.middleName + user.lastName]
      .filter(Boolean)
      .join(" ");
  };

  const handleEditClick = (index: number) => {
    const user = users[index];
    setEditIndex(index);
    setEditedUser({ ...user });
    setEditStudentID(user.studentID || "");
    setEditYearLevel(user.yearLevel || "1");
    setEditProgram(user.program || "");
    setEditCustomProgram(
      defaultPrograms.includes(user.program || "") ? "" : user.program || ""
    );
    setShowEditCustomProgramInput(!defaultPrograms.includes(user.program || ""));
    setValidationErrors({});
  };

  const validateFields = (user: any, isNewUser = false) => {
    const errors: Record<string, string> = {};

    if (!user.firstName.trim()) {
      errors.firstName = "First name is required";
    }

    if (!user.lastName.trim()) {
      errors.lastName = "Last name is required";
    }

    if (!user.email.trim()) {
      errors.email = "Email is required";
    } else if (!/\S+@\S+\.\S+/.test(user.email)) {
      errors.email = "Email is invalid";
    }

    if (isNewUser && !user.password.trim()) {
      errors.password = "Password is required";
    }

    if (user.role.length === 0) {
      errors.role = "At least one role must be selected";
    }

    return errors;
  };

  const handleSaveChanges = async () => {
    const errors = validateFields(editedUser);

    if (editedUser.role.includes("Student")) {
      if (!editStudentID.trim()) {
        errors.studentId = "Student ID is required for Student role";
      }
      if (!editYearLevel) {
        errors.yearLevel = "Year level is required for Student role";
      }
      if (!editProgram && !editCustomProgram) {
        errors.program = "Program is required for Student role";
      }
    }

    if (Object.keys(errors).length > 0) {
      setValidationErrors(errors);
      return;
    }

    try {
      // Only update student if the role is Student
      if (editedUser.role.includes("Student") && editIndex !== null) {
        const studentId = users[editIndex].studentID;
        const studentData = {
          firstName: editedUser.firstName,
          middleName: editedUser.middleName,
          lastName: editedUser.lastName,
          email: editedUser.email,
          id: editStudentID,
          yearLevel: editYearLevel,
          program: editProgram === "Other (Please specify)" ? editCustomProgram : editProgram,
        };

        const response = await fetch(`${API_BASE_URL}/updateStudent/${studentId}`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(studentData),
        });

        if (!response.ok) {
          throw new Error('Failed to update student');
        }

        const updatedStudent = await response.json();
        
        // Update local state
        const updatedUsers = [...users];
        updatedUsers[editIndex] = {
          ...updatedStudent,
          role: ["Student"],
          profilePic: editProfilePicPreview || users[editIndex].profilePic,
        };
        setUsers(updatedUsers);
      } else {
        // For non-student roles, just update local state
        const updatedUsers = [...users];
        updatedUsers[editIndex!] = {
          ...editedUser,
          profilePic: editProfilePicPreview || users[editIndex!].profilePic,
        };
        setUsers(updatedUsers);
      }

      setEditProfilePic(null);
      setEditProfilePicPreview("");
      setEditIndex(null);
      setValidationErrors({});
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to update student');
    }
  };

  const handleDeleteClick = (index: number) => {
    setDeleteIndex(index);
  };

  const handleConfirmDelete = async () => {
    if (deleteIndex === null) return;

    try {
      const userToDelete = users[deleteIndex];
      
      // Only call API if the user is a student
      if (userToDelete.role.includes("Student") && userToDelete.studentID) {
        const response = await fetch(`${API_BASE_URL}/deleteStudent/${userToDelete.studentID}`, {
          method: "DELETE",
        });

        if (!response.ok) {
          throw new Error('Failed to delete student');
        }
      }

      // Update local state
      const updatedUsers = users.filter((_, i) => i !== deleteIndex);
      setUsers(updatedUsers);
      setDeleteIndex(null);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to delete student');
    }
  };

  const toggleRoleSelection = (
    role: string,
    roles: string[],
    setRoles: (updatedRoles: string[]) => void
  ) => {
    const newRoles = roles.includes(role)
      ? roles.filter((r) => r !== role)
      : [...roles, role];

    if (role === "Student") {
      setShowStudentFields(newRoles.includes("Student"));
    }

    setRoles(newRoles);
  };

  const handleProgramSelect = (selectedProgram: string) => {
    if (selectedProgram === "Other (Please specify)") {
      setShowCustomProgramInput(true);
      setProgram(selectedProgram);
    } else {
      setShowCustomProgramInput(false);
      setProgram(selectedProgram);
      setCustomProgram("");
    }
    setProgramDropdownOpen(false);
  };

  const handleEditProgramSelect = (selectedProgram: string) => {
    if (selectedProgram === "Other (Please specify)") {
      setShowEditCustomProgramInput(true);
      setEditProgram(selectedProgram);
    } else {
      setShowEditCustomProgramInput(false);
      setEditProgram(selectedProgram);
      setEditCustomProgram("");
    }
    setEditProgramDropdownOpen(false);
  };

  const programMap: Record<string, number> = {
    "BS Computer Engineering": 1,
    "BS Civil Engineering": 2,
    "BS Electronics Engineering": 3,
    "BS Electrical Engineering": 4,
    // Add other programs as needed
  };


  const handleAddUser = async () => {
    const errors = validateFields(newUser, true);

    if (newUser.role.includes("Student")) {
      if (!studentID.trim()) {
        errors.studentId = "Student ID is required for Student role";
      }
      if (!yearLevel) {
        errors.yearLevel = "Year level is required for Student role";
      }
      if (!program && !customProgram) {
        errors.program = "Program is required for Student role";
      }
    }

    if (Object.keys(errors).length > 0) {
      setValidationErrors(errors);
      return;
    }

    try {
      let newUserObject: any = {
        firstName: newUser.firstName,
        middleName: newUser.middleName,
        lastName: newUser.lastName,
        email: newUser.email,
        profilePic: profilePicPreview || "",
      };

      if (newUser.role.includes("Student")) {
        const selectedProgram = program === "Other (Please specify)" ? customProgram : program;
        const programID = programMap[selectedProgram];
        
        if (isNaN(programID)) {
          throw new Error('Invalid program selected');
        }

        const studentData = {
          studentID: studentID,
          studentName: `${newUser.firstName} ${newUser.middleName || ''} ${newUser.lastName}`.trim(),
          email: newUser.email,
          password: newUser.password,
          programID: programID,
          yearLevel: parseInt(yearLevel),
          photo: profilePicPreview || null
        };

        const response = await fetch(`${API_BASE_URL}/createStudent`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(studentData),
        });

        if (!response.ok) {
          throw new Error('Failed to create student');
        }

        const createdStudent = await response.json();
        newUserObject = {
          ...createdStudent,
          firstName: newUser.firstName, // Split name back for frontend display
          middleName: newUser.middleName,
          lastName: newUser.lastName,
          studentID: createdStudent.studentID,
          profilePic: profilePicPreview || "",
        };
      } else {
        // For non-student roles, just add to local state
        newUserObject = {
          ...newUserObject,
          password: newUser.password,
        };
      }

      // Update local state
      setUsers([...users, newUserObject]);
      setProfilePic(null);
      setProfilePicPreview("");
      setAddUserModalOpen(false);
      setNewUser({
        firstName: "",
        middleName: "",
        lastName: "",
        email: "",
        password: "",
        role: [],
      });
      setStudentID("");
      setYearLevel("1");
      setProgram("");
      setCustomProgram("");
      setShowStudentFields(false);
      setShowCustomProgramInput(false);
      setValidationErrors({});
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to create user');
    }
  };

  const getRoleBadge = (role: string) => {
    let badgeClass = "";
    switch (role) {
      case "Admin":
        badgeClass = "badge bg-primary";
        break;
      case "Student":
        badgeClass = "badge bg-success";
        break;
      case "SSG Officer":
      case "Event Organizer":
        badgeClass = "badge bg-warning";
        break;
      default:
        badgeClass = "badge bg-secondary";
    }
    return <span className={badgeClass}>{role}</span>;
  };

  const filteredUsers = users.filter((user) => {
    const fullName = getFullName(user);
    return [
      fullName,
      user.email,
      user.role.join(", "),
      user.studentID || "",
      user.yearLevel || "",
      user.program || "",
    ]
      .join(" ")
      .toLowerCase()
      .includes(searchTerm.toLowerCase());
  });

  if (isLoading) {
    return <div>Loading users...</div>;
  }

  if (error) {
    return <div className="alert alert-danger">Error: {error}</div>;
  }

  return (
    <div className="manage-users-page">
      <NavbarAdmin />
      <div className="manage-users-container">
        <header className="manage-users-header">
          <h2>User Management</h2>
          <p className="subtitle">
            View and manage all system users and their permissions
          </p>
        </header>

        {/* Search Bar */}
        <div className="search-container">
          <div className="search-box">
            <img src={search_logo} alt="search" className="search-icon" />
            <input
              type="search"
              placeholder="Search users by name, email or role..."
              className="search-input"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>
          <button
            className="btn btn-primary add-user-btn"
            onClick={() => {
              setAddUserModalOpen(true);
              setValidationErrors({});
            }}
          >
            <AiOutlineUserAdd /> Add New User
          </button>
        </div>

        {/* Users Table */}
        <div className="table-responsive">
          <table className="users-table">
            <thead>
              <tr>
                <th>Name</th>
                <th>Email</th>
                <th>Details</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {filteredUsers.map((user, index) => (
                <tr key={index}>
                  {/* Name + Avatar Column */}
                  <td data-label="Name">
                    <div className="user-with-avatar">
                      {user.profilePic && (
                        <img
                          src={user.profilePic}
                          alt="Profile"
                          className="user-avatar"
                        />
                      )}
                      {getFullName(user)}
                    </div>
                  </td>

                  {/* Email Column */}
                  <td data-label="Email">{user.email}</td>

                  {/* Details Column */}
                  <td data-label="Details">
                    <div>
                      {user.role.includes("Student") && (
                        <>
                          {user.studentID && (
                            <div className="student-id">
                              ID: {user.studentID}
                            </div>
                          )}
                          {user.yearLevel && (
                            <div className="year-level">
                              Year: {user.yearLevel}
                            </div>
                          )}
                          {user.program && (
                            <div className="program">
                              Program: {user.program}
                            </div>
                          )}
                        </>
                      )}
                      <div className="role-badges">
                        {user.role.map((role, i) => (
                          <span key={i}>{getRoleBadge(role)}</span>
                        ))}
                      </div>
                    </div>
                  </td>

                  {/* Actions Column */}
                  <td data-label="Actions" className="actions-cell">
                    <div className="button-group">
                      <button
                        className="btn btn-info"
                        onClick={() => handleEditClick(index)}
                      >
                        <AiFillEdit /> Edit
                      </button>
                      <button
                        className="btn btn-danger"
                        onClick={() => handleDeleteClick(index)}
                      >
                        <AiFillCloseCircle /> Delete
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
              {filteredUsers.length === 0 && (
                <tr>
                  <td colSpan={4} className="no-results">
                    No matching users found. Try a different search term.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>

        {/* Add User Modal */}

        <Modal
          isOpen={addUserModalOpen}
          onRequestClose={() => {
            setAddUserModalOpen(false);
            setValidationErrors({});
          }}
          className="user-modal"
          overlayClassName="modal-overlay"
        >
          <div className="modal-header">
            <h3>Add New User</h3>
            <button
              onClick={() => {
                setAddUserModalOpen(false);
                setValidationErrors({});
              }}
              className="close-button"
            >
              &times;
            </button>
          </div>
          <div className="modal-body">
            <div className="form-group">
              <label htmlFor="firstName">First Name</label>
              <input
                type="text"
                id="firstName"
                placeholder="First Name"
                value={newUser.firstName}
                onChange={(e) =>
                  setNewUser({ ...newUser, firstName: e.target.value })
                }
                className={validationErrors.firstName ? "input-error" : ""}
              />
              {validationErrors.firstName && (
                <div className="error-message">
                  {validationErrors.firstName}
                </div>
              )}
            </div>

            <div className="form-group">
              <label htmlFor="middleName">Middle Name (Optional)</label>
              <input
                type="text"
                id="middleName"
                placeholder="Middle Name"
                value={newUser.middleName}
                onChange={(e) =>
                  setNewUser({ ...newUser, middleName: e.target.value })
                }
              />
            </div>

            <div className="form-group">
              <label htmlFor="lastName">Last Name</label>
              <input
                type="text"
                id="lastName"
                placeholder="Last Name"
                value={newUser.lastName}
                onChange={(e) =>
                  setNewUser({ ...newUser, lastName: e.target.value })
                }
                className={validationErrors.lastName ? "input-error" : ""}
              />
              {validationErrors.lastName && (
                <div className="error-message">{validationErrors.lastName}</div>
              )}
            </div>

            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                type="email"
                id="email"
                placeholder="Email"
                value={newUser.email}
                onChange={(e) =>
                  setNewUser({ ...newUser, email: e.target.value })
                }
                className={validationErrors.email ? "input-error" : ""}
              />
              {validationErrors.email && (
                <div className="error-message">{validationErrors.email}</div>
              )}
            </div>

            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input
                type="password"
                id="password"
                placeholder="Password"
                value={newUser.password}
                onChange={(e) =>
                  setNewUser({ ...newUser, password: e.target.value })
                }
                className={validationErrors.password ? "input-error" : ""}
              />
              {validationErrors.password && (
                <div className="error-message">{validationErrors.password}</div>
              )}
            </div>

            {showStudentFields && (
              <>
                <div className="form-group">
                  <label htmlFor="studentId">Student ID</label>
                  <input
                    type="text"
                    id="studentId"
                    placeholder="Student ID"
                    value={studentID}
                    onChange={(e) => setStudentID(e.target.value)}
                    className={validationErrors.studentID ? "input-error" : ""}
                  />
                  {validationErrors.studentId && (
                    <div className="error-message">
                      {validationErrors.studentId}
                    </div>
                  )}
                </div>
                <div className="form-group">
                  <label htmlFor="yearLevel">Year Level</label>
                  <select
                    id="yearLevel"
                    value={yearLevel}
                    onChange={(e) => setYearLevel(e.target.value)}
                    className={validationErrors.yearLevel ? "input-error" : ""}
                  >
                    {yearLevels.map((level) => (
                      <option key={level} value={level}>
                        {level}
                      </option>
                    ))}
                  </select>
                  {validationErrors.yearLevel && (
                    <div className="error-message">
                      {validationErrors.yearLevel}
                    </div>
                  )}
                </div>

                <div className="form-group">
                  <label>Profile Picture (For Face Recognition)</label>
                  <div className="profile-pic-upload">
                    {profilePicPreview ? (
                      <div className="profile-pic-preview">
                        <img src={profilePicPreview} alt="Preview" />
                        <button
                          type="button"
                          className="btn btn-sm btn-outline-secondary"
                          onClick={() => {
                            setProfilePic(null);
                            setProfilePicPreview("");
                            if (fileInputRef.current)
                              fileInputRef.current.value = "";
                          }}
                        >
                          Change
                        </button>
                      </div>
                    ) : (
                      <div className="upload-area">
                        <input
                          type="file"
                          ref={fileInputRef}
                          accept="image/*"
                          onChange={handleProfilePicChange}
                          style={{ display: "none" }}
                        />
                        <button
                          type="button"
                          className="btn btn-outline-primary"
                          onClick={() => fileInputRef.current?.click()}
                        >
                          Upload Picture
                        </button>
                        <p className="upload-hint">
                          Recommended: Clear face photo
                        </p>
                      </div>
                    )}
                  </div>
                </div>
                <div className="form-group">
                  <label>Program</label>
                  <div className="dropdown-wrapper">
                    <div className="dropdown">
                      <button
                        type="button"
                        className={`dropdown-btn ${
                          validationErrors.program ? "input-error" : ""
                        }`}
                        onClick={() =>
                          setProgramDropdownOpen(!programDropdownOpen)
                        }
                      >
                        {program || "Select Program"}
                        <span className="icon">
                          {programDropdownOpen ? "▲" : "▼"}
                        </span>
                      </button>
                      {validationErrors.program && (
                        <div className="error-message">
                          {validationErrors.program}
                        </div>
                      )}
                      {programDropdownOpen && (
                        <div className="dropdown-content">
                          {defaultPrograms.map((programOption) => (
                            <label
                              key={programOption}
                              className="dropdown-item radio-style"
                            >
                              <input
                                type="radio"
                                name="program"
                                checked={program === programOption}
                                onChange={() =>
                                  handleProgramSelect(programOption)
                                }
                                className="radio-input"
                              />
                              <span className="radio-custom"></span>
                              {programOption}
                            </label>
                          ))}
                        </div>
                      )}
                    </div>
                  </div>
                </div>

                {showCustomProgramInput && (
                  <div className="form-group">
                    <label htmlFor="customProgram">Specify Program</label>
                    <input
                      type="text"
                      id="customProgram"
                      placeholder="Enter your program"
                      value={customProgram}
                      onChange={(e) => setCustomProgram(e.target.value)}
                      className={validationErrors.program ? "input-error" : ""}
                    />
                  </div>
                )}
              </>
            )}

            <div className="form-group">
              <label>Roles</label>
              <div className="dropdown-wrapper">
                <div className="dropdown">
                  <button
                    type="button"
                    className={`dropdown-btn ${
                      validationErrors.role ? "input-error" : ""
                    }`}
                    onClick={() => setRoleDropdownOpen(!roleDropdownOpen)}
                  >
                    {newUser.role.length > 0 ? (
                      <div className="selected-roles">
                        {newUser.role.map((role) => (
                          <span key={role} className="selected-role-badge">
                            {role}
                          </span>
                        ))}
                      </div>
                    ) : (
                      <span>Select Roles</span>
                    )}
                    <span className="icon">{roleDropdownOpen ? "▲" : "▼"}</span>
                  </button>
                  {validationErrors.role && (
                    <div className="error-message">{validationErrors.role}</div>
                  )}
                  {roleDropdownOpen && (
                    <div className="dropdown-content">
                      {availableRoles.map((role) => (
                        <label key={role} className="dropdown-item radio-style">
                          <input
                            type="checkbox"
                            checked={newUser.role.includes(role)}
                            onChange={() =>
                              toggleRoleSelection(role, newUser.role, (roles) =>
                                setNewUser({ ...newUser, role: roles })
                              )
                            }
                            className="radio-input"
                          />
                          <span className="radio-custom"></span>
                          {role}
                        </label>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            </div>
          </div>
          <div className="modal-footer">
            <button
              className="btn btn-secondary"
              onClick={() => {
                setAddUserModalOpen(false);
                setValidationErrors({});
              }}
            >
              Cancel
            </button>
            <button className="btn btn-primary" onClick={handleAddUser}>
              Add User
            </button>
          </div>
        </Modal>

        {/* Edit User Modal */}
        <Modal
          isOpen={editIndex !== null}
          onRequestClose={() => {
            setEditIndex(null);
            setValidationErrors({});
          }}
          className="user-modal"
          overlayClassName="modal-overlay"
        >
          <div className="modal-header">
            <h3>Edit User</h3>
            <button
              onClick={() => {
                setEditIndex(null);
                setValidationErrors({});
              }}
              className="close-button"
            >
              &times;
            </button>
          </div>
          <div className="modal-body">
            <div className="form-group">
              <label htmlFor="editFirstName">First Name</label>
              <input
                type="text"
                id="editFirstName"
                value={editedUser.firstName}
                onChange={(e) =>
                  setEditedUser({ ...editedUser, firstName: e.target.value })
                }
                className={validationErrors.firstName ? "input-error" : ""}
              />
              {validationErrors.firstName && (
                <div className="error-message">
                  {validationErrors.firstName}
                </div>
              )}
            </div>

            <div className="form-group">
              <label htmlFor="editMiddleName">Middle Name (Optional)</label>
              <input
                type="text"
                id="editMiddleName"
                value={editedUser.middleName}
                onChange={(e) =>
                  setEditedUser({ ...editedUser, middleName: e.target.value })
                }
              />
            </div>

            <div className="form-group">
              <label htmlFor="editLastName">Last Name</label>
              <input
                type="text"
                id="editLastName"
                value={editedUser.lastName}
                onChange={(e) =>
                  setEditedUser({ ...editedUser, lastName: e.target.value })
                }
                className={validationErrors.lastName ? "input-error" : ""}
              />
              {validationErrors.lastName && (
                <div className="error-message">{validationErrors.lastName}</div>
              )}
            </div>

            <div className="form-group">
              <label htmlFor="editEmail">Email</label>
              <input
                type="email"
                id="editEmail"
                value={editedUser.email}
                onChange={(e) =>
                  setEditedUser({ ...editedUser, email: e.target.value })
                }
                className={validationErrors.email ? "input-error" : ""}
              />
              {validationErrors.email && (
                <div className="error-message">{validationErrors.email}</div>
              )}
            </div>

            {editedUser.role.includes("Student") && (
              <>
                <div className="form-group">
                  <label htmlFor="editStudentId">Student ID</label>
                  <input
                    type="text"
                    id="editStudentId"
                    placeholder="Student ID"
                    value={editStudentID}
                    onChange={(e) => setEditStudentID(e.target.value)}
                    className={validationErrors.studentID ? "input-error" : ""}
                  />
                  {validationErrors.studentID && (
                    <div className="error-message">
                      {validationErrors.studentID}
                    </div>
                  )}
                </div>

                <div className="form-group">
                  <label htmlFor="editYearLevel">Year Level</label>
                  <select
                    id="editYearLevel"
                    value={editYearLevel}
                    onChange={(e) => setEditYearLevel(e.target.value)}
                    className={validationErrors.yearLevel ? "input-error" : ""}
                  >
                    {yearLevels.map((level) => (
                      <option key={level} value={level}>
                        {level}
                      </option>
                    ))}
                  </select>
                  {validationErrors.yearLevel && (
                    <div className="error-message">
                      {validationErrors.yearLevel}
                    </div>
                  )}
                </div>

                <div className="form-group">
                  <label>Profile Picture (For Face Recognition)</label>
                  <div className="profile-pic-upload">
                    {editProfilePicPreview || users[editIndex!]?.profilePic ? (
                      <div className="profile-pic-preview">
                        <img
                          src={
                            editProfilePicPreview ||
                            users[editIndex!].profilePic
                          }
                          alt="Preview"
                        />
                        <button
                          type="button"
                          className="btn btn-sm btn-outline-secondary"
                          onClick={() => editFileInputRef.current?.click()}
                        >
                          Change
                        </button>
                        <input
                          type="file"
                          ref={editFileInputRef}
                          accept="image/*"
                          onChange={handleEditProfilePicChange}
                          style={{ display: "none" }}
                        />
                      </div>
                    ) : (
                      <div className="upload-area">
                        <input
                          type="file"
                          ref={editFileInputRef}
                          accept="image/*"
                          onChange={handleEditProfilePicChange}
                          style={{ display: "none" }}
                        />
                        <button
                          type="button"
                          className="btn btn-outline-primary"
                          onClick={() => editFileInputRef.current?.click()}
                        >
                          Upload Picture
                        </button>
                      </div>
                    )}
                  </div>
                </div>

                <div className="form-group">
                  <label>Program</label>
                  <div className="dropdown-wrapper">
                    <div className="dropdown">
                      <button
                        type="button"
                        className={`dropdown-btn ${
                          validationErrors.program ? "input-error" : ""
                        }`}
                        onClick={() =>
                          setEditProgramDropdownOpen(!editProgramDropdownOpen)
                        }
                      >
                        {editProgram ||
                          users[editIndex!]?.program ||
                          "Select Program"}
                        <span className="icon">
                          {editProgramDropdownOpen ? "▲" : "▼"}
                        </span>
                      </button>
                      {validationErrors.program && (
                        <div className="error-message">
                          {validationErrors.program}
                        </div>
                      )}
                      {editProgramDropdownOpen && (
                        <div className="dropdown-content">
                          {defaultPrograms.map((programOption) => (
                            <label
                              key={programOption}
                              className="dropdown-item radio-style"
                            >
                              <input
                                type="radio"
                                name="editProgram"
                                checked={
                                  editProgram === programOption ||
                                  (!editProgram &&
                                    users[editIndex!]?.program ===
                                      programOption) ||
                                  (programOption === "Other (Please specify)" &&
                                    !defaultPrograms.includes(
                                      users[editIndex!]?.program || ""
                                    ))
                                }
                                onChange={() =>
                                  handleEditProgramSelect(programOption)
                                }
                                className="radio-input"
                              />
                              <span className="radio-custom"></span>
                              {programOption}
                            </label>
                          ))}
                        </div>
                      )}
                    </div>
                  </div>
                </div>

                {showEditCustomProgramInput && (
                  <div className="form-group">
                    <label htmlFor="editCustomProgram">Specify Program</label>
                    <input
                      type="text"
                      id="editCustomProgram"
                      placeholder="Enter your program"
                      value={
                        editCustomProgram ||
                        (users[editIndex!]?.program &&
                        !defaultPrograms.includes(users[editIndex!].program)
                          ? users[editIndex!].program
                          : "")
                      }
                      onChange={(e) => setEditCustomProgram(e.target.value)}
                      className={validationErrors.program ? "input-error" : ""}
                    />
                  </div>
                )}
              </>
            )}

            <div className="form-group">
              <label>Roles</label>
              <div className="dropdown-wrapper">
                <div className="dropdown">
                  <button
                    type="button"
                    className={`dropdown-btn ${
                      validationErrors.role ? "input-error" : ""
                    }`}
                    onClick={() =>
                      setEditRoleDropdownOpen(!editRoleDropdownOpen)
                    }
                  >
                    {editedUser.role.length > 0 ? (
                      <div className="selected-roles">
                        {editedUser.role.map((role) => (
                          <span key={role} className="selected-role-badge">
                            {role}
                          </span>
                        ))}
                      </div>
                    ) : (
                      <span>Select Roles</span>
                    )}
                    <span className="icon">
                      {editRoleDropdownOpen ? "▲" : "▼"}
                    </span>
                  </button>
                  {validationErrors.role && (
                    <div className="error-message">{validationErrors.role}</div>
                  )}
                  {editRoleDropdownOpen && (
                    <div className="dropdown-content">
                      {availableRoles.map((role) => (
                        <label key={role} className="dropdown-item radio-style">
                          <input
                            type="checkbox"
                            checked={editedUser.role.includes(role)}
                            onChange={() =>
                              toggleRoleSelection(
                                role,
                                editedUser.role,
                                (roles) =>
                                  setEditedUser({ ...editedUser, role: roles })
                              )
                            }
                            className="radio-input"
                          />
                          <span className="radio-custom"></span>
                          {role}
                        </label>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            </div>
          </div>
          <div className="modal-footer">
            <button
              className="btn btn-secondary"
              onClick={() => {
                setEditIndex(null);
                setValidationErrors({});
              }}
            >
              Cancel
            </button>
            <button className="btn btn-primary" onClick={handleSaveChanges}>
              Save Changes
            </button>
          </div>
        </Modal>

        {/* Delete Confirmation Modal */}
        <Modal
          isOpen={deleteIndex !== null}
          onRequestClose={() => setDeleteIndex(null)}
          className="confirmation-modal"
          overlayClassName="modal-overlay"
        >
          <div className="modal-header">
            <h3>Confirm Deletion</h3>
          </div>
          <div className="modal-body">
            <p>Are you sure you want to delete this user?</p>
            {deleteIndex !== null && (
              <p className="user-to-delete">
                {getFullName(users[deleteIndex])} ({users[deleteIndex].email})
              </p>
            )}
          </div>
          <div className="modal-footer">
            <button
              className="btn btn-outline-secondary"
              onClick={() => setDeleteIndex(null)}
            >
              Cancel
            </button>
            <button className="btn btn-danger" onClick={handleConfirmDelete}>
              Delete User
            </button>
          </div>
        </Modal>
      </div>
    </div>
  );
};

export default ManageUsers;
